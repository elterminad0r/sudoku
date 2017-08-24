import sys
import argparse
import collections


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--empty", action="store_true", help="get an empty sudoku")
    return parser.parse_args()

sudo_tmp = ((((("{} " * 3
                  + " ") * 3)
                      + "\n") * 3
                          + "\n") * 3)

def print_sud(sud):
    print(sudo_tmp.format(*sud))

row_sets = [{i * 9 + j for j in range(9)} for i in range(9)]
col_sets = [{j * 9 + i for j in range(9)} for i in range(9)]
box_sets = [{h * 27 + i * 3 + j + k * 9 for j in range(3) for k in range(3)} for h in range(3) for i in range(3)]
all_sets = row_sets + col_sets + box_sets

square_membergroups = [list({j for group in all_sets
                               for j in group
                               if i in group})
                       for i in range(81)]

def solve(sud, empty_indices):
    if not empty_indices:
        yield sud
    else:
        nxt = empty_indices.popleft()
        for i in range(1, 10):
            if not any(sud[prev] == i for prev in square_membergroups[nxt]):
                sud[nxt] = i
                yield from solve(sud, empty_indices)
            sud[nxt] = 0
        empty_indices.appendleft(nxt)

def read_sud(f):
    return list(map(int, f.read().split()))

def empty_sud():
    return [0 for _ in range(81)]

def main():
    args = parse_args()
    if args.empty:
        print_sud(empty_sud())
    else:
        sud = read_sud(sys.stdin)
        empty_indices = collections.deque(ind for ind, i in enumerate(sud) if not i)

        for s in solve(sud, empty_indices):
            print_sud(s)

if __name__ == "__main__":
    main()
