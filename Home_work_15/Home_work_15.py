def eratosthenes_generator(end):
    sieve = [True] * (end + 1)
    sieve[0] = sieve[1] = False

    for current in range(2, int(end ** 0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, end + 1, current):
                sieve[multiple] = False

    for num in range(2, end + 1):
        if sieve[num]:
            yield num


def prime_numbers(start, end):
    for prime in eratosthenes_generator(end):
        if prime >= start:
            yield prime


start = 2
end = 50

print(f"Prime numbers from {start} to {end}:")
for num in prime_numbers(start, end):
    print(num, end=", ")
