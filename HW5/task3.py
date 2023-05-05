def findLIS(a):
    n = len(a)           # размер исходного массива
    prev = [-1] * n      # массив, хранящий индексы предыдущих элементов в НВП
    d = [1] * n          # массив, хранящий длины НВП для каждого элемента массива

    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j   # запоминаем индекс предыдущего элемента в НВП

    pos = 0               # индекс последнего элемента в НВП
    length = d[0]         # длина НВП
    for i in range(n):
        if d[i] > length:
            pos = i       # обновляем индекс последнего элемента в НВП
            length = d[i] # обновляем длину НВП

    answer = []
    while pos != -1:
        answer.append(a[pos])
        pos = prev[pos]   # восстанавливаем НВП, переходя к предыдущему элементу

    answer.reverse()     # переворачиваем список, чтобы он был в порядке возрастания

    return answer

if __name__ == '__main__':
    import random
    N = 20
    a = [random.randint(-100, 100) for _ in range(N)]
    print('a', a)
    print('LIS', findLIS(a))
