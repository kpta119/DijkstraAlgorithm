from dijkstra import find_start_end, find_path, dijkstra, print_path
import sys


def load_board(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.strip())) for line in file]


def main(filename):
    board = load_board(filename)
    start, end = find_start_end(board)
    parents = dijkstra(board, start)
    path = find_path(parents, start, end)
    print_path(board, path)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        arg = 'graph.txt'
    main(arg)
