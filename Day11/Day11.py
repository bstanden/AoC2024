# AoC 2024
# Day 11
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 55312


def get_stone_count(s, max_depth, stones_map, depth=0):
    if s in stones_map:
        if depth in stones_map[s]:
            return stones_map[s][depth]
    else:
        stones_map[s] = dict()

    if depth == max_depth:
        stones_map[s][depth] = 1
    elif s == 0:
        stones_map[s][depth] = get_stone_count(1, max_depth, stones_map, depth + 1)
    elif not (s_len := len(s_str := str(s))) % 2:
        stones_map[s][depth] = (get_stone_count(int(s_str[s_len // 2:]), max_depth, stones_map, depth + 1)
                                + get_stone_count(int(s_str[0:s_len // 2]), max_depth, stones_map, depth + 1))
    else:
        stones_map[s][depth] = get_stone_count(s * 2024, max_depth, stones_map, depth + 1)

    return stones_map[s][depth]


def do_puzzle1(i):
    stone_map=dict()
    return sum([get_stone_count(s, 25, stone_map) for s in sorted([int(n) for n in i[0].split(" ")])])


def do_puzzle2(i):
    stone_map=dict()
    return sum([get_stone_count(s, 75, stone_map) for s in sorted([int(n) for n in i[0].split(" ")])])


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

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
