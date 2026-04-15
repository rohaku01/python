def climb_stairs_memo(n, memo={}):
    """Dynamic programming with memoization"""
    # Check if we've already calculated this value
    if n in memo:
        return memo[n]  # Return cached result - O(1) lookup!
    
    # Base cases
    if n <= 2:
        return n
    
    # Calculate once and store in memo for future use
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]

print(climb_stairs_memo(5))

# Call: climb_stairs_memo(5)
#   memo = {} (empty)
  
#   Call: climb_stairs_memo(4) 
#     memo = {} (empty)
    
#     Call: climb_stairs_memo(3)
#       memo = {} (empty)
      
#       Call: climb_stairs_memo(2) → returns 2 (base case)
#       Call: climb_stairs_memo(1) → returns 1 (base case)
      
#       Result: 2 + 1 = 3
#       memo = {3: 3} (stored!)
    
#     Call: climb_stairs_memo(2) → returns 2 (base case)
    
#     Result: 3 + 2 = 5
#     memo = {3: 3, 4: 5} (stored!)
  
#   Call: climb_stairs_memo(3) → returns 3 (FROM MEMO - no recursion!)
  
#   Result: 5 + 3 = 8
#   memo = {3: 3, 4: 5, 5: 8}