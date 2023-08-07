fibonacci_value_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
####################### 0  1  2  3  4  5  6  7    8  9   10  11  12   13    14   15   16   17    18    19

def count_fibonacci_number(n: int):
    if n == 1 or n == 2:
        return 1
    return count_fibonacci_number(n - 1) + count_fibonacci_number(n - 2)


print(count_fibonacci_number(13))
