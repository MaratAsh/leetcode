# Hint 1

Use dynamic programming approach. Build dp table where dp[a][b][c] is the number of ways you can start building the array starting from index a where the search_cost = c and the maximum used integer was b.

# Hint 2

Recursively, solve the small sub-problems first. Optimize your answer by stopping the search if you exceeded k changes.
