#Задание 1: Изоморфизмы
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for c1, c2 in zip(s, t):
        # Проверка существующего соответствия
        if c1 in map_st:
            if map_st[c1] != c2:
                return False
        else:
            map_st[c1] = c2

        # Обратная проверка (важно!)
        if c2 in map_ts:
            if map_ts[c2] != c1:
                return False
        else:
            map_ts[c2] = c1

    return True
# Пример
s = 'paper'
t = 'title'
print('Задание 1: Изоморфизмы')
print(is_isomorphic(s, t))


#Задание 2: Натуральная последовательность
def missing_number(nums):
    n = len(nums) + 1  # потому что одного числа не хватает
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
# Пример
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print('Задание 2: Натуральная последовательность')
print(missing_number(nums))


#Задание 3: Факторизация
def prime_factors(n: int):
    factors = []

    # 1. Обрабатываем двойку
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # 2. Проверяем нечётные числа
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # 3. Если осталось простое число
    if n > 1:
        factors.append(n)

    return factors
# Пример
n = 56
print('Задание 3: Факторизация')
print(prime_factors(n))