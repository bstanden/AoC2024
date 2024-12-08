# AoC 2024
# Day8
#
# Dr Bob

import itertools

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 14
PUZZLE_2_TEST_RESULT = 34


def parse_data(input):
    frequencies = set([c for i in input for c in i if c != "."])
    transmitters = dict()
    for f in frequencies:
        transmitters[f] = [(x, y) for y in range(len(input)) for x in range(len(input[0])) if input[y][x] == f]
    return transmitters


def get_antinodes(transmitters, lim_x, lim_y, resonance=False):
    antinodes = set()
    for t in transmitters.values():
        for a, b in list(itertools.combinations(t, 2)):
            a_x, a_y = a
            b_x, b_y = b
            delta_x = b_x - a_x
            delta_y = b_y - a_y

            while 0 <= a_x < lim_x and 0 <= a_y < lim_y:
                if resonance or (a_x, a_y) != a:
                    antinodes.add((a_x, a_y))
                if not resonance and (a_x, a_y) != a:
                    break
                a_x = a_x - delta_x
                a_y = a_y - delta_y
            while 0 <= b_x < lim_x and 0 <= b_y < lim_y:
                if resonance or (b_x, b_y) != b:
                    antinodes.add((b_x, b_y))
                if not resonance and (b_x, b_y) != b:
                    break
                b_x = b_x + delta_x
                b_y = b_y + delta_y
    return antinodes


def do_puzzle1(input):
    return len(get_antinodes(parse_data(input), len(input[0]), len(input)))


def do_puzzle2(input):
    return len(get_antinodes(parse_data(input), len(input[0]), len(input), resonance=True))


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
