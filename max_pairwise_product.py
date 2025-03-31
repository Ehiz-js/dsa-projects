
import random


def max_pairwise_product(numbers):
    length = len(numbers)
    max_product = 0
    for first in range(length):
        for second in range(first + 1, length):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
def max_pairwise_product_fast(numbers):
    max_1 = max(numbers)
    max_1_index = numbers.index(max_1)
    numbers.remove(numbers[max_1_index])
    max_2 = max(numbers)
    return max_1 * max_2
def max_pairwise_product_fast2(numbers):
    first_max = second_max = float('-inf')
    for num in numbers:
        if num > first_max:
            second_max, first_max = first_max, num
        elif num > second_max:
            second_max = num
    return first_max * second_max


if __name__ == '__main__':
    while True:
        n = random.randint(2,11)
        print(n)
        a = list()
        for i in range(n):
            a.append(random.randint(1, 100000))
        for i in range(n):
            print(a[i])
        res1 = max_pairwise_product_fast(a)
        res2 = max_pairwise_product_fast2(a)
        if res1!=res2:
            print("Wrong Answer: "+res1+" "+res2)
            break
        else:
            print("OK")

    # _ = int(input())
    # input_numbers = list(map(int, input().split()))
    # print(max_pairwise_product_fast(input_numbers))
