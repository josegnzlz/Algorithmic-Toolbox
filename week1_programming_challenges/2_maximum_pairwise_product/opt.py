def max_pairwise_product(numbers):
    n = len(numbers)
    high_number1 = 0
    high_number2 = 0
    for first in range(n):
        if numbers[first] >= high_number1:
            high_number2 = high_number1
            high_number1 = numbers[first]
        elif numbers[first] > high_number2:
            high_number2 = numbers[first]
    max_product = high_number1 * high_number2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
