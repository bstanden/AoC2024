# AoC 2024
# Day 7
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 3749
PUZZLE_2_TEST_RESULT = 11387


def to_base(i, b):
    if i == 0:
        return "0"

    ret_val = ""
    while i > 0:
        ret_val = str(i % b) + ret_val
        i //= b
    return ret_val


def is_solution(solution, parameters, operators):
    result = parameters[0]
    for i, o in enumerate(operators):
        match o:
            case '0':
                result = result + parameters[i + 1]
            case '1':
                result = result * parameters[i + 1]
            case '2':
                result = int(str(result) + str(parameters[i + 1]))

        if result > solution:
            return False

    return result == solution


def has_solution(solution, parameters, op_list):
    num_operators = len(parameters) - 1

    if not num_operators:
        return "0" if solution == parameters[0] else False

    for perm in range(op_list ** num_operators):
        operators = ("0" * num_operators + to_base(perm, op_list))[-num_operators:]
        if is_solution(solution, parameters, [o for o in operators]):
            return True

    return False


def parse_data(input):
    return [(int(i.split(":")[0]), [int(p) for p in i.split(":")[1][1:].split(" ")]) for i in input]


def solve_calibrations(input, op_list):
    calibrations = parse_data(input)
    solvable = [has_solution(solution, parameters, op_list) for solution, parameters in calibrations]
    return sum([calibrations[i][0] for i, s in enumerate(solvable) if s])


def do_puzzle1(input):
    return solve_calibrations(input, 2)


def do_puzzle2(input):
    return solve_calibrations(input, 3)


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle1(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE))
    print(f"puzzle1 result: {result}")

    # puzzle 2 example
    result = do_puzzle2(read_file(INPUT_FILE_TEST))
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
