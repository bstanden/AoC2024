# AoC 2024
# Day5
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 143
PUZZLE_2_TEST_RESULT = 123


def parse_data(input):
    split_idx = input.index('')
    rules = [[int(x) for x in p.split("|")] for p in input[:split_idx]]
    pages = [[int(i) for i in p.split(',')] for p in input[split_idx + 1:]]
    return rules, pages, [get_rules_validity(rules, p) for p in pages]


def get_rules_validity(rules, p):
    return all([True if a not in p or b not in p or p.index(a) < p.index(b) else False for a, b in rules])


def reorder(p, rules):
    f_rules = [(x, y) for x, y in rules if x in p and y in p]
    ret_val = [p.pop()]
    while len(p):
        c = p.pop()
        for i in range(len(ret_val) + 1):
            ret_val.insert(i, c)
            if get_rules_validity(f_rules, ret_val):
                break
            ret_val.pop(i)
    return ret_val


def do_puzzle1(input):
    rules, pages, validity = parse_data(input)
    return sum([p[int(len(p) / 2)] for i, p in enumerate(pages) if validity[i]])


def do_puzzle2(input):
    rules, pages, validity = parse_data(input)
    reordered = [reorder(p, rules) for i, p in enumerate(pages) if not validity[i]]
    return sum([p[int(len(p) / 2)] for i, p in enumerate(reordered)])


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
