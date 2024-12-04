# AoC 2024
# Day 2
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 2
PUZZLE_2_TEST_RESULT = 4

def is_safe( ints ):
    deltas = [ints[n + 1] - ints[n] for n in range(len(ints) - 1)]
    return (1 if
            ((all([d > 0 for d in deltas]) or all([d < 0 for d in deltas]))
            and max([abs(d) for d in deltas]) <= 3)
             else 0)

def do_puzzle1(input):
    return sum([is_safe([int(n) for n in i.split(" ")]) for i in input])


def do_puzzle2(input):
    safe = 0
    for i in input:
        ints = [int(n) for n in i.split(" ")]
        safe = safe + (1 if any([is_safe(l) for l in [ ints[:n] + ints[n + 1:] for n in range(len(ints))]])else 0)
    return safe


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
