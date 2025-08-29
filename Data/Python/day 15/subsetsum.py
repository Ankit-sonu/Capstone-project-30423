def is_subset_sum_dp(arr, total):
    n = len(arr)
    dp = [[False] * (total + 1) for _ in range(n + 1)]

    # Sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the subset table
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

    return dp[n][total]

# Example
arr = [3, 34, 4, 12, 5, 2]
#[3,4,12,2], [4,12,5],
target = 21
print("Is Subset Sum:", is_subset_sum_dp(arr, target))