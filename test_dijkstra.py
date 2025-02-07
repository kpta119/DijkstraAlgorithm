from dijkstra import find_start_end, extract_min, dijkstra, find_path


def testFindStartAndEnd():
    graph = [
        [1, 2, 1, 0],
        [2, 4, 3, 5],
        [1, 0, 9, 2]
    ]
    start, end = find_start_end(graph)
    assert start == (0, 3)
    assert end == (2, 1)


def testExtractMinFromQueue():
    queue = [(1, 1), (0, 1), (1, 0)]
    distances = [[0, 6], [8, 5]]
    removedFromQueue = extract_min(queue, distances)
    assert removedFromQueue == (1, 1)


def testDijsktraFunction1():
    graph = [
        [2, 0, 5],
        [4, 1, 4],
        [8, 2, 0]
    ]
    start = (0, 1)
    parents = dijkstra(graph, start)
    assert parents[2][2] == (2, 1)
    assert parents[2][1] == (1, 1)
    assert parents[1][1] == (0, 1)


def testDijsktraFunction2():
    graph = [
        [3, 0, 2],
        [2, 4, 1],
        [8, 5, 0]
    ]
    start = (0, 1)
    parents = dijkstra(graph, start)
    assert parents[2][2] == (1, 2)
    assert parents[1][2] == (0, 2)
    assert parents[0][2] == (0, 1)


def testFindPathFunction():
    graph = [
        [0, 1, 2],
        [2, 4, 1],
        [8, 5, 0]
    ]
    start = (0, 0)
    end = (2, 2)
    parents = dijkstra(graph, start)
    path = find_path(parents, start, end)
    assert path[0] == start
    assert path[1] == (0, 1)
    assert path[2] == (0, 2)
    assert path[3] == (1, 2)
    assert path[4] == end


def testFindPathFunction2():
    graph = [
        [2, 0, 5],
        [4, 1, 4],
        [8, 2, 0]
    ]
    start = (0, 1)
    end = (2, 2)
    parents = dijkstra(graph, start)
    path = find_path(parents, start, end)
    assert path[0] == start
    assert path[1] == (1, 1)
    assert path[2] == (2, 1)
    assert path[3] == end
