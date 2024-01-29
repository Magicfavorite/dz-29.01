list_ = [5, 2, 1, 4, 10, 6, 27, 8, 9, 2, -2]

def min_func(list_, m=None):
    if not list_:
        return m
    elif not m or m > list_[0]:
        m = list_[0]
    return min_func(list_[1:], m)


print(min_func(list_))

