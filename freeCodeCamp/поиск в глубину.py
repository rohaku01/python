def dfs(graph, start):
    visited = set()
    
    def dfs_recursive(vertex):
        visited.add(vertex)
        print(f"  Посетили вершину {vertex}")  
        for n in range(len(graph)):
            if graph[vertex][n] != 0 and n not in visited:
                print(f"    Из {vertex} идем в {n}")
                dfs_recursive(n)
    
    dfs_recursive(start)
    return list(visited)

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))