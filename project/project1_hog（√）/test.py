from operator import add
def next_hail(k):
    if k % 2 == 0:
        return k // 2
    else:
        return 3 * k + 1


def hail_tally(n, f):   # 返回 序列N和方法f
    total = 0
    while n > 1:
        total = f(total, n)
        n = next_hail(n)
    return f(total, 1)


def sum_some(select):
    def f(total, k):
        if select(k):
            return add(total, k)
        return total
    return f


# 1
def below_ten(k):
    return k < 10


sum_below_ten = sum_some(below_ten)
hail_tally(3, sum_below_ten)
