# AoC 2024
# Day 4
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 18
PUZZLE_2_TEST_RESULT = 9


def safe_get_char(x, y, input):
    return input[y][x] if (0 <= x < len(input[0])) and (0 <= y < len(input)) else "."


def do_puzzle1(input):
    match_string = "XMAS"

    directions = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]
    return sum([[all([safe_get_char(x + dx * n, y + dy * n, input) == match_string[n]
                      for n in range(len(match_string))])
                 for dx, dy in directions].count(True)
                for x in range(len(input[0])) for y in range(len(input))])


def do_puzzle2(input):
    return [(input[y][x] == "A" and
             ({safe_get_char(x - 1, y - 1, input), safe_get_char(x + 1, y + 1, input)}
              == {safe_get_char(x - 1, y + 1, input), safe_get_char(x + 1, y - 1, input)}
              == {"M", "S"}))
            for x in range(len(input[0])) for y in range(len(input))].count(True)


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
