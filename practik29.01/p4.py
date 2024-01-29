def my_func(num,d):
    a = 0
    while d in num: num.remove(d); a += 1
    return a



print(my_func([2,3,5,5,6,4], 5))
