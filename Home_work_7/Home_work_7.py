# 1. Create a file with numbers (in a few rows)

def calculate_sum_from_file(filename):
    total_sum = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())  # Convert line to a floating-point number
                    total_sum += number
                except ValueError:
                    # Handle non-numeric entries here
                    print(f"Ignored non-numeric entry: {line.strip()}")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

    return total_sum


if __name__ == "__main__":
    filename = "test.txt"
    total = calculate_sum_from_file(filename)
    print(f"The sum of all numbers in '{filename}' is: {total}")

#
#
# # print(sum_of_numbers(345, 890))
#
# try:
#     print(sum_of_numbers("Hello", 890))
# except ValueError:
#     print("One of the values is not a number")
