#  1. Напишіть функцію, яка приймає два аргументи.
#  a. Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
#  b. Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
#  c. В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

def conditions_for_arguments(one_argument, two_argument):
    if type(one_argument) == int and type(two_argument) == int:
        return one_argument * two_argument
    elif type(one_argument) == str and type(two_argument) == str:
        return one_argument + " " + two_argument
    else:
        return one_argument, two_argument


if __name__ == '__main__':
    operations_arguments = conditions_for_arguments(3, 3)
    print(operations_arguments)
    print("Internal module")
