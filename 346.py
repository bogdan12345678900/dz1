data = {'a': 5, 'b': 1, 'c': 8, 'd': 3}
threshold = 4
for key in list(data.keys()):
    if data[key] < threshold:
        del data[key]
print("Оновлений словник:", data)
