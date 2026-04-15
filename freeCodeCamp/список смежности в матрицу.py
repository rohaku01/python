def adjacency_list_to_matrix(my_dict):
    n = len(my_dict)

    matrix = [[0]*n for _ in range(n)]

    for i,k in my_dict.items():
        for j in k:
            matrix[i][j] = 1
    for row in matrix:
        print(row)

    return matrix

adj_list = {
    0: [2],
    1: [2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

adjacency_list_to_matrix(adj_list)