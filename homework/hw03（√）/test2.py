def my_sum_iter(s):
    value = 0
    for i in range(len(s)):
        value += s[i]
    return value


print(my_sum_iter([1, 2, 3, 4]))

def my_sum_recur(k):
    if k == []:
        return 0
    else:
        return k[0] + my_sum_iter(k[1:])

print(my_sum_recur([1,2,3,4]))
