def num_1(*args):
    count = 0

    for num in args:
        if is_prime(num):
            count += 1
    return count

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime

print(num_1(-2, 2, 3, 5, 10))
