
numbers = [4, 5, 6, 3, 9]
def my_func(numbers, k):
    return [x ** k for x in numbers]

print(my_func(numbers, 2))
