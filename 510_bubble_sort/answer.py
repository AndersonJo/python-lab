def bubble_sort(data):
    count = len(data) - 1
    while count >= 0:
        for j in range(count):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        count -= 1
    return data
