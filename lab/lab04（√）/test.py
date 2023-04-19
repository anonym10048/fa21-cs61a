def coords(fn, seq, lower, upper):
    return [[seq[i], fn(seq[i])] for i in range(len(seq)) if lower <= fn(seq[i]) <= upper]

seq = [-4, -2, 0, 1, 3]
fn = lambda x: x**2
print(coords(fn, seq, 1, 9))