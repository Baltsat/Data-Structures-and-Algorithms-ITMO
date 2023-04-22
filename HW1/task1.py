def find(numbers: list, target: int, steps: int):
    if len(numbers) == 1:
        if numbers[0] == target:
            return steps+1
        else:
            return 'not found'
    elif len(numbers) == 2:
        if numbers[0] == target or numbers[1] == target:
            return steps+1
        else:
            return 'not found'
    else:
        mid = numbers[len(numbers)//2]
        if target == mid:
            return steps+1
        elif target < mid:
            return find(numbers[:len(numbers)//2], target, steps+1)
        elif target > mid:
            return find(numbers[len(numbers)//2+1:], target, steps+1)


if __name__ == '__main__':
    numbers = []

    for i in range(1, 100):
        numbers.append(i)

    numbers = sorted(numbers)

    target = 39

    print(find(numbers, target, 0))
