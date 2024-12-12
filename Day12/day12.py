# AoC 2024
# Day1 n
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 1930
PUZZLE_2_TEST_RESULT = 1206


def count_vertices(plots, i, plot):
    count = 0

    for p in plot['extent']:
        fences = [(fp, fn) for (fp, fn) in plot['fences'] if fp == p]
        match len(fences):
            case 2:
                ((_), (ax, ay)), ((_), (bx, by)) = fences
                if ax != bx and ay != by:
                    count += 1
            case 3:
                count += 2
            case 4:
                count += 4

    for p in plot['extent']:
        count += [get_neighbour(i, p, (x1 + x2, y1 + y2))[1] != plot['plant'] and
                  (get_neighbour(i, p, (x1, y1))[1] == get_neighbour(i, p, (x2, y2))[1] == plot['plant'])
                  for ((x1, y1), (x2, y2)) in
                  [((0, -1), (-1, 0)), ((0, -1), (1, 0)), ((1, 0), (0, 1)), ((0, 1), (-1, 0))]].count(True)

    return count


def get_neighbour(i, p, d):
    x, y = p
    dx, dy = d
    nx = x + dx
    ny = y + dy
    return (nx, ny), i[ny][nx] if 0 <= ny < len(i) and 0 <= nx < len(i[0]) else "."


def get_plot(p, i, plot=None):
    if not plot:
        x, y = p
        plot = {'plant': i[y][x],
                'extent': [],
                'fences': []}
    plot['extent'].append(p)
    for (x, y), n in [get_neighbour(i, p, d) for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
        if n == plot['plant']:
            if not (x, y) in plot['extent']:
                get_plot((x, y), i, plot)
        else:
            plot['fences'].append([p, (x, y)])

    return plot


def do_puzzle1(i):
    plots = []
    for y in range(len(i)):
        for x in range(len(i[y])):
            if not any([(x, y) in p['extent'] for p in plots]):
                plots.append(get_plot((x, y), i))

    return sum([len(p['fences']) * len(p['extent']) for p in plots])


def do_puzzle2(i):
    plots = []
    for y in range(len(i)):
        for x in range(len(i[y])):
            if not any([(x, y) in p['extent'] for p in plots]):
                plots.append(get_plot((x, y), i))

    return sum([count_vertices(plots, i, p) * len(p['extent']) for p in plots])


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
