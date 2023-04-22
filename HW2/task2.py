def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    import random
    import timeit

    numbers = [random.randint(-1000, 1000) for i in range(1, 1000)]

    print(f"Sorted time: {timeit.timeit('sorted(numbers)', number=100, setup='from __main__ import numbers')}")
    print(f"Bubble_sort time: {timeit.timeit('bubble_sort(numbers)', number=100, setup='from __main__ import numbers, bubble_sort')}")

