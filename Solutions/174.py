def calculateMinimumHP(dungeon):
    M = len(dungeon)
    if M == 0:
        return 0
    N = len(dungeon[0])
    if N == 0:
        return 0
    dp = [[0 for _ in row] for row in dungeon]
    # Set health for last cell
    dp[M - 1][N - 1] = max(1, 1 - dungeon[M - 1][N - 1])
    # There's no choice for health on the Mth row and Nth column
    for i in reversed(range(0, M - 1)):
        dp[i][N - 1] = max(1, dp[i + 1][N - 1] - dungeon[i][N - 1])
    for j in reversed(range(0, N - 1)):
        dp[M - 1][j] = max(1, dp[M - 1][j + 1] - dungeon[M - 1][j])
    # Our goal is to minimize the health required, but clamp this value by the smallest health value
    for i in reversed(range(M - 1)):
        for j in reversed(range(N - 1)):
            dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
    return dp[0][0]








dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
a = calculateMinimumHP(dungeon)
print(a)