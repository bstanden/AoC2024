# AoC 2024
# Day 3
#
# Dr Bob

import re

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE_TEST_2 = "input_test_2.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 161
PUZZLE_2_TEST_RESULT = 48


def do_puzzle1(input):
    input_line="".join(input)
    sum=0
    for m in [m.start() for m in re.finditer('mul()', input_line)]:
        terminator_index=re.search(r'[^{0123456789,}]', input_line[m+4:]).start()
        if input_line[m+4+terminator_index]==")":
            operands=input_line[m+4:m+4+terminator_index]
            if operands.count(",")==1:
                a,b=input_line[m+4:m+4+terminator_index].split(",")
                sum=sum+(int(a)*int(b))

    return sum


def do_puzzle2(input):
    input_line="".join(input)
    sum=0
    do_index=[0]
    do_index.extend([m.start() for m in re.finditer('do\(\)', input_line)])
    do_not_index=[0]
    do_not_index.extend([m.start() for m in re.finditer("don\'t\(\)", input_line)])

    for m in [m.start() for m in re.finditer('mul()', input_line)]:
        terminator_index=re.search(r'[^{0123456789,}]', input_line[m+4:]).start()
        if input_line[m+4+terminator_index]==")":
            operands=input_line[m+4:m+4+terminator_index]
            if operands.count(",")==1 and max( [d for d in do_index if d < m]) >= max ( [d for d in do_not_index if d<m]):
                a,b=input_line[m+4:m+4+terminator_index].split(",")
                sum=sum+(int(a)*int(b))

    return sum

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
    result = do_puzzle2(read_file(INPUT_FILE_TEST_2))
    assert result == PUZZLE_2_TEST_RESULT, f"Failed Puzzle 2 assertion: expected {PUZZLE_2_TEST_RESULT}, got {result}"

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE))
    print(f"puzzle2 result: {result}")
