def is_prime_iter(n):
    """
    >>> is_prime_iter(1)
    False
    >>> is_prime_iter(2)
    True
    >>> is_prime_iter(16)
    False
    """
    if n == 1:
        return False
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return False
    return True


def is_prime_recur(n):
    """
    >>> is_prime_recur(1)
    False
    >>> is_prime_recur(2)
    True
    >>> is_prime_recur(16)
    False
    """
    if n == 1:
        return False

    def helper(i):
        if i == 1:
            return True
        elif n % i == 0:
            return False
        else:
            return helper(i - 1)
    return helper(n - 1)

