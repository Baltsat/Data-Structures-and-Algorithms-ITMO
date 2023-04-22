# Блочная сортировка (Bucket sort)
def bucket_sort(arr, num_buckets=20):
    # Создание "карманов" (buckets)
    buckets = [[] for _ in range(num_buckets)]

    # Распределение элементов по "карманам"
    for value in arr:
        index = int(value * num_buckets)
        buckets[index].append(value)

    # Сортировка элементов в каждом "кармане"
    for i in range(num_buckets):
        buckets[i].sort()

    # Объединение "карманов"
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += bucket

    return sorted_arr


# Пирамидальная сортировка (Heap sort)
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


# Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]

        return result

    return merge(left, right)
