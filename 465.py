def count(v):
    result = {}
    for i in v:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


v = ['Анна', 'Олег', 'Анна', 'Ірина', 'Олег', 'Анна']
print(count(v))

