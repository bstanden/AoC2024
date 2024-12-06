# AoC 2024
# Day 6
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 41
PUZZLE_2_TEST_RESULT = 6

d = "^>v<"


def get_start(input):
    start_y = ["^" in l for l in input].index(True)
    return input[start_y].index("^"), start_y


def solve_path(input):
    x, y = get_start(input)

    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0)
    }
    d_idx = 0

    path = {(x, y): "^"}

    while (True):
        new_x = x + directions[d[d_idx]][0]
        new_y = y + directions[d[d_idx]][1]

        if not (0 <= new_x < len(input[y]) and 0 <= new_y < len(input)):
            break
        elif input[new_y][new_x] == "#":
            d_idx = (d_idx + 1) % len(d)
        elif d[d_idx] in path.get((new_x, new_y), ""):
            return None
        else:
            x = new_x
            y = new_y
        path[(x, y)] = path.get((x, y), "") + d[d_idx]

    return path


def do_puzzle1(input):
    return len(solve_path(input))


def do_puzzle2(input):
    count = 0
    start_x, start_y = get_start(input)
    path = solve_path(input)

    for x, y in path:
        if not (x == start_x and y == start_y):
            input[y][x] = "#"
            if solve_path(input) is None:
                count = count + 1
            input[y][x] = "."

    return count


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [[c for c in e.strip()] for e in lines]


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
