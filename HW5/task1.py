def knapsack_greedy(n, m, k, items):
    items = sorted(items, key=lambda x: x[0], reverse=True)
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    total_weight = 0
    num_items = n
    stolen_items = []
    for i in range(m):
        weight_left = k
        for item in items:
            if weight_left == 0 or num_items == 0:
                break
            if item[0] <= weight_left and item not in stolen_items:
                weight_left -= item[0]
                total_value += item[1]
                total_weight += item[0]
                stolen_items.append(item)
                num_items -= 1
            elif item[0] > weight_left:
                continue
    return total_value, total_weight, stolen_items


if __name__=='__main__':
    items = [(1, 1), (2, 2), (3, 3), (3, 4), (4, 100)] # items = [(weight, value)]
    K = max_weight_per_visit = 3
    M = max_visits = 3
    N = 3

    total_value, total_weight, stolen_items = knapsack_greedy(N, M, K, items)
    print("Total value: ", total_value)
    print("Total weight: ", total_weight)
    print("Stolen items: ")
    for item in stolen_items:
        print("- ", item)

