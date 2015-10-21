def bubble_sort(data):
    N = len(data)
    count = N - 1
    while count > 0:
        for i in range(0, count):
            a, b = data[i], data[i + 1]
            if a > b:
                data[i] = b
                data[i + 1] = a

        count -= 1
    return data
