# DFS 03
graphs = {
    '1': ['2','3'],
    '2': ['5','6'],
    '3': ['7','4'],
    '4': [],
    '5': [],
    '6': [],
    '7': ['8'],
    '8': []
}
visited = set()

def DFS(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graphs[node]:
            DFS(neighbour)
DFS('1')
