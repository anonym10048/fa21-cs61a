
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def store_digits(n):
    if n < 10:
        return Link(n)
    k, m, flg = n // 10, n % 10, 1
    while k >= 10:
        flg += 1
        k, m = k // 10, m + k % 10 * 10 ** flg
    return Link(k, store_digits(m))


print(store_digits(2345).__repr__())


