def zad(arr):

    n = len(arr)-1 # liczba macierzy

    # minimalna maorzenia macierzy od i do j
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for L in range(2, n + 1):
        for j in range(L, n + 1):
            i = j - L +1
            dp[i][j] = float("inf")

            # punkt kodziału (mi ... mk) * (m k +1 .. mj)

            for k in range(i, j):
                nk = dp[i][k] + dp[k + 1][j] + (arr[i - 1] * arr[k] * arr[j])

                if nk < dp[i][j]:
                    dp[i][j] = nk


    for arr in dp:
        print(arr)

    return dp[1][-1]


arr = [10, 100, 1, 20, 10, 30]
zad(arr)
