# 1. Задача: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

operation_1 = (first * second) / 10 + second
operation_2 = (second - first) + (second % first)

print(operation_1)
print(operation_2)
print(type(operation_1))
print(type(operation_2))

print(operation_1 // operation_2)

# 2. Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

number_1 = 40
number_2 = 35

is_equal_1 = number_2 == number_1
is_not_equal = number_2 != number_1
is_less_or_equal = number_2 <= number_1
is_less_more_equal = number_2 >= number_1
print(is_equal_1, is_not_equal, is_less_or_equal, is_less_more_equal)

# 3.Задача: Створіть змінну - результат конкатенації строк "Hello " та "world!".
word_greeting = "Hello"
world_word = "world!"

print(word_greeting + " " + world_word)
