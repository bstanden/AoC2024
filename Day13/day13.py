# AoC 2024
# Day 13
#
# Dr Bob


INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 480


def get_xy(l, compensate=False):
    return [int(n.lstrip()[2:]) + (10000000000000 if compensate else 0) for n in l.split(":")[1].lstrip().split(",")]


def do_puzzle(i, compensate=False):  # find integer solutions using Cramer's rule
    return sum([(px * bdy - py * bdx) // det * 3 + (adx * py - ady * px) // det
                for adx, ady, bdx, bdy, px, py in
                [get_xy(i[n]) + get_xy(i[n + 1]) + get_xy(i[n + 2], compensate) for n in range(0, len(i), 4)]
                if not (px * bdy - py * bdx) % (det := (adx * bdy - bdx * ady)) and not (adx * py - ady * px) % det])


def do_puzzle1(i):
    return do_puzzle(i)


def do_puzzle2(i):
    return do_puzzle(i, compensate=True)


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
    result = do_puzzle2(read_file(INPUT_FILE_TEST))

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
