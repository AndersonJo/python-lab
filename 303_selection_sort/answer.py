def selection_sort(data):
    N = len(data)
    for end_point in range(N - 1, 0, -1):
        max_pos = 0
        for i in range(0, end_point + 1):
            if data[max_pos] < data[i]:
                max_pos = i
        data[end_point], data[max_pos] = data[max_pos], data[end_point]
    return data
