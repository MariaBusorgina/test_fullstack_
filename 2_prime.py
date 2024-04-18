def is_prime(number):
    """Функция принимает число и возвращает True, если число простое"""

    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def prime_numbers_in_range(min_numb, max_numb):
    """Функция возвращает список всех простых чисел в заданном диапазоне"""

    prime_numbers = []

    for number in range(min_numb, max_numb + 1):
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers

