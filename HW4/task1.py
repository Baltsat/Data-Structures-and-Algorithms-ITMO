# С использованием re
def count_numbers(string):
    import regex as re
    numbers = re.findall(r'\d{2}', string, overlapped=True)
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts

# Наивный алгоритм поиска подстрок
def naive_search(string, pattern_len=2):
    n = len(string)
    count_dict = {}
    for i in range(n - pattern_len + 1):
        pattern = string[i:i+pattern_len]
        if pattern.isdigit() and len(pattern) == pattern_len:
            if pattern in count_dict:
                count_dict[pattern] += 1
            else:
                count_dict[pattern] = 1
    sorted_counts = sorted(
        count_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


# Алгоритм Рабина-Карпа
def rabin_karp_search(string, pattern_len=2):
    # Задаем полиномиальную кольцевую!! hash-функцию.
    def H(substring: str, x=10, m=1):
        '''
        same as int
        '''
        h = 0
        for i in range(len(substring)):
            h += int(substring[i])*x**(m-i)
        return h
    counts = {f'{i:02}': 0 for i in range(1, 100)}
    hash_table = []
    for i in range(len(string) - pattern_len + 1):
        hash_table.append(H(string[i:i+pattern_len]))
    for pattern in counts.keys():
        pattern_hash = H(pattern)
        for hash in hash_table:
            if pattern_hash == hash:
                # Посимвольная проверка не требуется. В нашем случае hash-функция – кольцевая.
                counts[pattern] += 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


# Алгоритм Бойера-Мура
def boyer_moore_search(string):
    counts = {f'{i:02}': 0 for i in range(1, 100)}
    for pattern in counts.keys():
        pos = 1  # len(pattern)==2
        while pos < len(string):
            if (string[pos] == pattern[1]) is False:
                if string[pos] in pattern:
                    pos += 1  # len(pattern)==2
                else:
                    pos += 2
            elif (string[pos-1] == pattern[0]) is False:
                pos += 1
            else:
                counts[pattern] += 1
                pos += 1
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


# Алгоритм Кнута-Морриса-Пратта
def kmp_search(string: str):
    def prefix(s) -> list:
        n = len(s)
        pi = [0] * n  # создаем список для хранения значений префикс-функции
        for i in range(1, n):
            j = pi[i-1]
            while j > 0 and s[j] != s[i]:
                j = pi[j-1]
            if s[j] == s[i]:
                j += 1
            pi[i] = j
        return pi

    counts = {f'{i:02}': 0 for i in range(1, 100)}
    for pattern in counts.keys():
        P = prefix(pattern)
        k = 0
        for i in range(len(string)):
            while k > 0 and pattern[k] != string[i]:
                k = P[k-1]
            if pattern[k] == string[i]:
                k += 1
            if k == len(pattern):
                counts[pattern] += 1
                k = P[k-1]
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts


if __name__ == '__main__':
    import timeit
    first_items: int = 8
    number = 10

    # Создаем массив из первых 500 чисел Фибоначчи:
    fibonacci = [0, 1]
    for i in range(2, 500):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    # Объединяем числа в строку и заменяем пробелы на пустые символы:
    fibonacci_str = ''.join(map(str, fibonacci))
    fibonacci_str = fibonacci_str.replace(' ', '')

    re_counts_time = timeit.timeit(lambda: count_numbers(fibonacci_str), number=number)
    print(f"Время выполнения count_numbers: {re_counts_time:.6f} сек.")
    re_counts = count_numbers(fibonacci_str)
    print(f'Re_counts\n{re_counts[:first_items]}\n')

    naive_counts_time = timeit.timeit(lambda: naive_search(fibonacci_str), number=number)
    print(f"Время выполнения naive_search: {naive_counts_time:.6f} сек.")
    naive_counts = naive_search(fibonacci_str)
    print(f'Наивный алгоритм\n{naive_counts[:first_items]}\n')

    rk_counts_time = timeit.timeit(lambda: rabin_karp_search(fibonacci_str), number=number)
    print(f"Время выполнения rabin_karp_search: {rk_counts_time:.6f} сек.")
    rk_counts = rabin_karp_search(fibonacci_str)
    print(f'Алгоритм Рабина-Карпа\n{rk_counts[:first_items]}\n')

    bm_counts_time = timeit.timeit(lambda: boyer_moore_search(fibonacci_str), number=number)
    print(f"Время выполнения boyer_moore_search: {bm_counts_time:.6f} сек.")
    bm_counts = boyer_moore_search(fibonacci_str)
    print(f'Алгоритм Бойера-Мура\n{bm_counts[:first_items]}\n')

    kmp_counts_time = timeit.timeit(lambda: kmp_search(fibonacci_str), number=number)
    print(f"Время выполнения kmp_search: {kmp_counts_time:.6f} сек.")
    kmp_counts = kmp_search(fibonacci_str)
    print(f'Алгоритм Кнута-Морриса-Пратта\n{kmp_counts[:first_items]}\n')
