# Znajowanie maksimum
num = [291, 3, 1, 6, -1, 243, 6, 1, 9, 56, 79]


def maximum_list(numbers):
    max_numbers = 0
    for n in numbers:
        if n > max_numbers:
            max_numbers = n
    return max_numbers


print("Rozwiązanie 1 - Liczba maksymalna wynosi: {}".format(maximum_list(num)))


def division_list(numbers):
    return numbers[:len(numbers) // 2], numbers[len(numbers) // 2:]


def max_divide_win(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        list_1, list_2 = division_list(numbers)
        max_1 = maximum_list(list_1)
        max_2 = maximum_list(list_2)
        if max_1 > max_2:
            return max_1
        else:
            return max_2


print("Rozwiązanie 2 (dziel i zwyciężaj - Liczba maksymalna wynosi: {}".format(max_divide_win(num)))
