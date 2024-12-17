def reverse(a):
    return {v: k for k, v in a.items()}


a = {'a': 1, 'b': 2, 'c': 3}
reversed = reverse(a)
print(reversed)

