# AoC 2024
# Day8
#
# Dr Bob

import itertools

import numpy

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


def trace_antinodes(antinodes, start, delta, lim_x, lim_y, resonance):
    x, y = start
    while 0 <= x < lim_x and 0 <= y < lim_y:
        if resonance or ((x, y) != start):
            antinodes.add((x, y))
        if not resonance and (x, y) != start:
            break
        x, y = numpy.add((x, y), delta)


def get_antinodes(transmitters, lim_x, lim_y, resonance=False):
    antinodes = set()
    for t in transmitters.values():
        for a, b in list(itertools.combinations(t, 2)):
            trace_antinodes(antinodes, a, numpy.subtract(a, b), lim_x, lim_y, resonance)
            trace_antinodes(antinodes, b, numpy.subtract(b, a), lim_x, lim_y, resonance)
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
