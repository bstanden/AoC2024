# AoC 2024
# Day 6
#
# Dr Bob

import copy

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 41
PUZZLE_2_TEST_RESULT = 6


def solve_path(input):
    y = ["^" in l for l in input].index(True)
    x = input[y].index("^")

    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0)
    }
    d = "^>v<"
    d_idx = 0

    while (True):
        new_x = x + directions[d[d_idx]][0]
        new_y = y + directions[d[d_idx]][1]

        if not (0 <= new_x < len(input[y]) and 0 <= new_y < len(input)):
            break
        elif input[new_y][new_x] == "#":
            d_idx = (d_idx + 1) % len(d)
        elif d[d_idx] in input[new_y][new_x]:
            return None
        else:
            x = new_x
            y = new_y
        input[y][x] = input[y][x] + d[d_idx]

    return len([c for l in input for c in l if not set(c).isdisjoint(d)])


def do_puzzle1(input):
    return solve_path(input)


def do_puzzle2(input):
    count = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] == ".":
                test_input = copy.deepcopy(input)
                test_input[y][x] = "#"
                if solve_path(test_input) is None:
                    count = count + 1
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
