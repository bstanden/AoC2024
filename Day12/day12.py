# AoC 2024
# Day1 n
#
# Dr Bob

INPUT_FILE_TEST = "input_test.txt"
INPUT_FILE = "input.txt"

PUZZLE_1_TEST_RESULT = 1930
PUZZLE_2_TEST_RESULT = 1206


def count_vertices(i, plot):
    count = 0

    for p in plot['extent']:
        match len(fences := [(fp, fn) for (fp, fn) in plot['fences'] if fp == p]):
            case 2:
                ((_), (ax, ay)), ((_), (bx, by)) = fences
                if ax != bx and ay != by:
                    count += 1
            case 3:
                count += 2
            case 4:
                count += 4

    count += sum([[get_neighbour(i, p, (a[0] + b[0], a[1] + b[1]))[1] != plot['plant'] and
                   (get_neighbour(i, p, a)[1] == get_neighbour(i, p, b)[1] == plot['plant'])
                   for p in plot['extent']
                   for (a,b) in
                   [((0, -1), (-1, 0)), ((0, -1), (1, 0)), ((1, 0), (0, 1)), ((0, 1), (-1, 0))]].count(True)])

    return count


def get_neighbour(i, p, d):
    nx,ny=tuple(sum(pair) for pair in zip(p, d))
    return (nx, ny), i[ny][nx] if 0 <= ny < len(i) and 0 <= nx < len(i[0]) else "."


def get_plot(p, i, plot=None):
    if not plot:
        x, y = p
        plot = {'plant': i[y][x], 'extent': [], 'fences': []}
    plot['extent'].append(p)
    for (x, y), n in [get_neighbour(i, p, d) for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
        if n == plot['plant']:
            if not (x, y) in plot['extent']:
                get_plot((x, y), i, plot)
        else:
            plot['fences'].append([p, (x, y)])

    return plot


def get_plots(i):
    plots = []
    _=[plots.append(get_plot((x, y), i)) for y in range(len(i))  for x in range(len(i[y])) if not any([(x, y) in p['extent'] for p in plots])]
    return plots

def do_puzzle1(i):
    return sum([len(p['fences']) * len(p['extent']) for p in get_plots(i)])


def do_puzzle2(i):
    return sum([count_vertices(i, p) * len(p['extent']) for p in get_plots(i)])


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
