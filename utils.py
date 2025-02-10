def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def is_perfect(number):
    factors = []

    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    if sum(factors) == number:
        return True
    return False

def properties(number):
    number = abs(number)
    properties = []
    number_as_string = str(number)
    len_of_number = len(number_as_string)

    sum = 0

    for i in number_as_string:
        sum += int(i) ** len_of_number

    if sum == number:
        properties.append('armstrong')

    # Add the right parity of the number
    if number % 2 == 0:
        properties.append('even')
    else:
        properties.append('odd')

    return properties

def digit_sum(number):
    number = abs(number)
    sum = 0

    for i in str(number):
        sum += int(i)
    return sum
