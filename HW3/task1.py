def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    swapped = True
    i = 0

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        i = 0
        swapped = False
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1

    return arr


if __name__ == '__main__':
    import timeit
    import sys
    sys.setrecursionlimit(10000)  # устанавливаем максимальную глубину рекурсии в 10000

    arr = [i for i in range(1000)]

    # Измеряем время выполнения быстрой сортировки
    quick_sort_time = timeit.timeit(lambda: quick_sort(arr), number=1000)
    print(f"Время выполнения быстрой сортировки: {quick_sort_time:.6f} сек.")

    # Измеряем время выполнения сортировки расческой
    comb_sort_time = timeit.timeit(lambda: comb_sort(arr), number=1000)
    print(f"Время выполнения сортировки расческой: {comb_sort_time:.6f} сек.")
