# def climb_stairs_optimized(n):
#     if n <= 2:
#         return n
    
#     prev2, prev1 = 1, 2  # Only store last two values
#     for i in range(3, n + 1):
#         current = prev1 + prev2
#         prev2, prev1 = prev1, current
#     return prev1

def climb_stairs_tabulation(n):
    """Dynamic programming with tabulation"""
    if n <= 2:
        return n
    
    # Create array to store results for all steps from 0 to n
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1
    dp[2] = 2  # 2 ways to reach step 2
    
    # Build up the solution iteratively
    for i in range(3, n + 1):
        # Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


print(climb_stairs_tabulation(5))

# Initial state:
# dp = [0, 1, 2, 0, 0, 0]
#      [0, 1, 2, 3, 4, 5] ← indices (step numbers)

# Step by step construction:

# i = 3:
#   dp[3] = dp[2] + dp[1] = 2 + 1 = 3
#   dp = [0, 1, 2, 3, 0, 0]
  
# i = 4:
#   dp[4] = dp[3] + dp[2] = 3 + 2 = 5
#   dp = [0, 1, 2, 3, 5, 0]
  
# i = 5:
#   dp[5] = dp[4] + dp[3] = 5 + 3 = 8
#   dp = [0, 1, 2, 3, 5, 8]

# Final result: dp[5] = 8