# Write generator, which generates numbers in a given range (from a certain number to a certain number)
def sum_range_of_numbers(first_number, last_number):
    actual = first_number
    while actual <= last_number:
        yield actual
        actual += 1


# Example usage
beginning_point = int(input("Enter the start number: "))
finishing_point = int(input("Enter the end number: "))
for num in sum_range_of_numbers(beginning_point, finishing_point):
    print(num)
