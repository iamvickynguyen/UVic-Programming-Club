def knapsack(items, maxWeight):
    n = len(items)
    dp = [[0 for i in range(maxWeight + 1)] for j in range(n + 1)]

    for r in range(n+1):
        for c in range(maxWeight + 1):
            if r == 0 or c == 0:
                dp[r][c] = 0
            elif int(items[r - 1]['weight']) <= c:
                dp[r][c] = max(dp[r - 1][c - int(items[r - 1]['weight'])] + int(items[r - 1]['value']), dp[r - 1][c])
            else:
                dp[r][c] = dp[r - 1][c]
    
    res = dp[n][maxWeight]
    w = maxWeight
    i = n
    objs = []
    while i > 0 and res > 0:
        if res != dp[i - 1][w]:
            objs.append(items[i-1])
            res -= int(items[i - 1]['value'])
            w -= int(items[i - 1]['weight'])
        i -= 1

    return objs