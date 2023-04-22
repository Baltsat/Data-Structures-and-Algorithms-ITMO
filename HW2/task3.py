# Алгоритм со сложностью O(3*n):
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                print(matrix[i][j][k], end=" ")
            print()
        print()
# Пример использования
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print_matrix(matrix)


# Алгоритм со сложностью O(n*log(n)):
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]

    return res


# Алгоритм со сложностью O(n!):
def permute(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        for j in permute(nums[:i] + nums[i+1:]):
            res.append([nums[i]] + j)
    return res


# Алгоритм со сложностью O(n^3):
def matrix_multiplication(a, b):
    m = len(a)
    n = len(b)
    p = len(b[0])

    res = [[0 for j in range(p)] for i in range(m)]

    for i in range(m):
        for j in range(p):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]

    return res

# Пример использования
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
c = matrix_multiplication(a, b)
print(c)


# Алгоритм со сложностью O(3*log(n)):
import math
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def log_loop(n):
    arr = [i for i in range(n)]
    for i in range(int(math.log(n, 2))):
        for j in range(int(math.log(n, 2))):
            x = binary_search(arr, j)
            if x != -1:
                print(i, j, x)

# Пример использования
log_loop(16)