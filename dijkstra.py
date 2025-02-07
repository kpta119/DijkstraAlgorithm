def find_start_end(board):
    start = None
    end = None
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == 0:
                if start is None:
                    start = (r, c)
                else:
                    end = (r, c)
    return start, end


def extract_min(queue, distances):
    min_index = None
    min_distance = float('inf')
    for i in range(len(queue)):
        if distances[queue[i][0]][queue[i][1]] < min_distance:
            min_index = i
            min_distance = distances[queue[i][0]][queue[i][1]]
    return queue.pop(min_index)


def dijkstra(board, start):
    rows = len(board)
    cols = len(board[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]
    parents = [[None] * cols for _ in range(rows)]

    distances[start[0]][start[1]] = 0
    queue = [(start[0], start[1])]

    while queue:
        current = extract_min(queue, distances)
        visited[current[0]][current[1]] = True

        for directionrow, directioncol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            newrow = current[0] + directionrow
            newcolumn = current[1] + directioncol
            if (
                (0 <= newrow < rows)
                and (0 <= newcolumn < cols)
                and (not visited[newrow][newcolumn])
            ):
                alt = (
                    distances[current[0]][current[1]]
                    + board[newrow][newcolumn]  
                    )
                if alt < distances[newrow][newcolumn]:
                    distances[newrow][newcolumn] = alt
                    parents[newrow][newcolumn] = current
                    queue.append((newrow, newcolumn))
    return parents


def find_path(parents, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parents[current[0]][current[1]]
    path.append(start)
    return path[::-1]


def print_path(board, path):
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols):
            if (r, c) in path:
                print(board[r][c], end=' ')
            else:
                print(' ', end=' ')
        print()  # \n
