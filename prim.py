
# Implementation of Prim's Algorithm

INF = float('inf')

def prim(graph, start):
    vertices = len(graph)
    selected = [False] * vertices

    selected[start] = True
    total_cost = 0

    print("Edge \tWeight")

    for _ in range(vertices - 1):
        minimum = INF
        x = 0
        y = 0

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x} - {y}\t{minimum}")
        total_cost += minimum
        selected[y] = True

    print("Total Minimum Cost:", total_cost)


# Graph represented using an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph, 0)
