def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS string
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_str.reverse()
    return dp[m][n], ''.join(lcs_str)

# Example
X = "ABCBDAB"
Y = "BDCAB"
length, sequence = lcs(X, Y)
print(f"LCS Length: {length}")
print(f"LCS: {sequence}")