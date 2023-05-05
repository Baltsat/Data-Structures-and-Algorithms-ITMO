def matrix_multiply_cost(matrix_list):
    n = len(matrix_list)
    dp = [[0] * n for _ in range(n)]
    
    # заполняем диагональные элементы нулями
    for i in range(n):
        dp[i][i] = 0
    
    # перебираем все возможные отрезки и находим минимальное количество скалярных операций
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1]
                dp[i][j] = min(dp[i][j], cost)
    
    # возвращаем минимальное количество скалярных операций
    return dp[0][n-1]

if __name__=='__main__':
    matrix_list = [(5, 10), (10, 20), (20, 35)]
    print(matrix_multiply_cost(matrix_list))  # Output: 4500
