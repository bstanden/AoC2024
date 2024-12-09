# AoC 2024
# Day 9
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 1928
PUZZLE_2_TEST_RESULT = 2858


def parse_data(input):
    files = [(int(id), int(len)) for id, len in enumerate(input[::2])]
    gaps = [(int(id), int(len)) for id, len in enumerate(input[1::2])]
    return files, gaps


def defrag(files, gaps):
    disk = []

    ld = len = 0
    while files:
        file = files.pop(0)
        if not files:
            f_id, f_len = file
            if id == f_id:
                disk.append((id, len + f_len))
            else:
                disk.append(file)
                disk.append((id, len))
                break
        disk.append(file)
        gap_id, gap = gaps.pop(0)

        while gap:
            if not len:
                if files:
                    id, len = files.pop()
                    if not files:
                        pass
                else:
                    break

            if len <= gap:
                disk.append((id, len))
                gap = gap - len
                if files:
                    id, len = files.pop()
                    if not files:
                        disk.append((id, len))
                        break

            else:
                disk.append((id, gap))
                len = len - gap
                break

    print(f"id={id}, len={len}")
    return disk


def checksum(disk):
    ret_val = 0
    pos = 0
    for id, len in disk:
        for n in range(len):
            ret_val = ret_val + (pos * id)
            pos = pos + 1
    return ret_val


def do_puzzle1(input):
    files, gaps = parse_data(input[0])
    disk = defrag(files, gaps)

    return checksum(disk)


def update_pos(pos, delta_pos):
    previous = pos[0]
    pos[0] += delta_pos
    return previous


def do_puzzle2(input):
    if len(input[0]) % 2 != 0:
        input[0] = input[0] + "0"

    pos = [0]
    disk = {p: {"start": update_pos(pos, length + gap), "len": length, "gap": gap}
            for p, (length, gap) in
            enumerate([(int(input[0][i]), int(input[0][i + 1])) for i in range(0, len(input[0]), 2)])}

    for file in range(len(disk) - 1, 0, -1):
        sorted_files = sorted(disk, key=lambda x: disk[x]["start"])
        for f in sorted_files:
            if disk[file]['start'] <= disk[f]['start']:
                break
            elif disk[f]['gap'] >= disk[file]['len']:
                for q in disk:
                    if disk[q]['start'] + disk[q]['len'] + disk[q]['gap'] == disk[file]['start']:
                        disk[q]['gap'] = disk[q]['gap'] + disk[file]['gap'] + disk[file]['len']
                        break
                disk[file]['gap'] = disk[f]['gap'] - disk[file]['len']
                disk[file]['start'] = disk[f]['start'] + disk[f]['len']
                disk[f]['gap'] = 0
                break

    return sum([pos * q for q in disk for pos in range(disk[q]['start'], disk[q]['start'] + disk[q]['len'])])


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
