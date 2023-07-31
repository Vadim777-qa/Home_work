# 1. Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".

input_string = ''
while 1:
    your_word = input("Type your word: ")
    if "o" in your_word:
        break
    input_string += your_word
print("There is an 'o' character in your word(s) ")

# 2. Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [x for x in lst1 if type(x) == str]
print(lst2)

# 3. Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
numbers_lst = [70, 22, 3, 44, 87, 1, 30, 10]
even_nos = [num for num in numbers_lst if num % 2 == 0]
print("Even numbers in the list: ", even_nos)
print("Sum of the even numbers: ", len(even_nos))


