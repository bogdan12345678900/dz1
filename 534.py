def lists_to_dict(k, v):
    result = {}
    for i in range(len(k)):
        result[k[i]] = v[i]
    return result



k = ['name', 'age', 'city']
v = ['Андрій', 25, 'Київ']
result = lists_to_dict(k , v)
print(result)

