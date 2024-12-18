# AoC 2024
# Day 10
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 36
PUZZLE_2_TEST_RESULT = 81


def parse_data(i):
    data = [[int(c) if c.isdigit() else -1 for c in line] for line in i]
    return data, [(x, y) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] == 0]


def get_point(p, data):
    x, y = p
    return data[y][x] if 0 <= y < len(data) and 0 <= x < len(data[y]) else -1


def get_neighbours(p, data):
    return [np for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if get_point(np := (p[0] + d[0], p[1] + d[1]), data) == get_point(p, data) + 1]


def distinct_paths(p, data) -> set:
    return {p} if get_point(p, data) == 9 else set().union(*[distinct_paths(n, data) for n in get_neighbours(p, data)])


def num_paths(p, data) -> int:
    return 1 if get_point(p, data) == 9 else sum([num_paths(n, data) for n in get_neighbours(p, data)])


def do_puzzle1(i):
    data, start = parse_data(i)
    return sum([len(p) for p in [distinct_paths(s, data) for s in start]])


def do_puzzle2(i):
    data, start = parse_data(i)
    return sum([p for p in [num_paths(s, data) for s in start]])


# slurp file into a list
def read_file(_filename):
    return  [line.rstrip() for line in open(_filename, 'r')]


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
