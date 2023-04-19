def cycle(f1, f2, f3):
    def curry1(n):
        def curry2(m):
            if n == 0:
                return m
            elif n % 3 == 1:
                return f1(curry1(n - 1)(m))
            elif n % 3 == 2:
                return f2(curry1(n - 1)(m))
            else:
                return f3(curry1(n - 1)(m))
        return curry2
    return curry1


def add1(x):
    return x + 1
def times2(x):
    return x * 2
def add3(x):
    return x + 3
my_cycle = cycle(add1, times2, add3)
add_one_then_double = my_cycle(2)
print(add_one_then_double(1))


