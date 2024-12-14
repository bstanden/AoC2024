# AoC 2024
# Day1 n
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 12


class Robot:
    def __init__(self, r_str, size_x, size_y):
        self._posx, self._posy, self._vx, self._vy = [int(i) for r_sub in r_str.split(" ") for i in
                                                      r_sub[2:].split(",")]
        self._size_x, self._size_y = size_x, size_y

    def move(self, seconds):
        self._posx = (self._posx + seconds * self._vx) % self._size_x
        self._posy = (self._posy + seconds * self._vy) % self._size_y

    def getLocation(self):
        return self._posx, self._posy

    def getQuadrant(self):
        middle_x = self._size_x // 2
        middle_y = self._size_y // 2
        return (
            True if self._posx < middle_x else False if self._posx > middle_x else None,
            True if self._posy < middle_y else False if self._posy > middle_y else None)


def do_puzzle1(input, size_x, size_y):
    robots = [Robot(l, size_x, size_y) for l in input]
    for r in robots:
        r.move(100)
    q = [r.getQuadrant() for r in robots]

    m = 1
    for d in [(True, True), (True, False), (False, True), (False, False)]:
        m = m * q.count(d)
    return m


def do_puzzle2(i, size_x, size_y):
    robots = [Robot(l, size_x, size_y) for l in i]
    secs = 0
    while (True):
        pos = set([r.getLocation() for r in robots])
        # puzzle instructions say that "most robots form a picture of a christmas tree"
        # I just assume that this means that more than half of occupied positions are next to another occupied
        # position - the "robots" are normally quite spread out.
        if [any([(px + dx, py + dy) in pos
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]]) # check each occupied position for a neighbour
            for px, py in pos].count(True) > len(pos) // 2:
            for y in range(0, size_y):
                for x in range(0, size_x):
                    print("*" if (x, y) in pos else " ", end="")
                print()
            return secs
        for r in robots:
            r.move(1)
        secs += 1


# slurp file into a list
def read_file(_filename):
    with open(_filename, 'r') as f:
        lines = f.readlines()
    return [e.strip() for e in lines]


# check we're being run directly
if __name__ == '__main__':
    # assertions against known, worked examples
    # puzzle 1 example
    result = do_puzzle1(read_file(INPUT_FILE_TEST), 11, 7)
    assert result == PUZZLE_1_TEST_RESULT, f"Failed Puzzle 1 assertion: expected {PUZZLE_1_TEST_RESULT}, got {result}"

    # puzzle 1
    result = do_puzzle1(read_file(INPUT_FILE), 101, 103)
    print(f"puzzle1 result: {result}")

    # puzzle 2
    result = do_puzzle2(read_file(INPUT_FILE), 101, 103)
    print(f"puzzle2 result: {result}")
