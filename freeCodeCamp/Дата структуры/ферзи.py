def dfs_n_queens(n):
    if n < 1:
        return []
    
    solutions = []
    board = [-1] * n
    
    def is_safe(row, col):
        for i in range(row):
            if board[i] == col:
                return False
            if board[i] - i == col - row:
                return False
            if board[i] + i == col + row:
                return False
        return True
    
    def dfs(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                dfs(row + 1)
                board[row] = -1
    
    dfs(0)
    return solutions

print(dfs_n_queens(5))