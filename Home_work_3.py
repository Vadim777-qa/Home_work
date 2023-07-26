unique_symbols = input("Enter your string to count symbols: ")
result = len(set(unique_symbols))
print(f"Number of symbols: {result}")

if result > 10:
    print("Your number has more than 10 unique symbols: " + "True")
else:
    print("Your number has less than 10 unique symbols: " + "False")