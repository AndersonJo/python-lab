def insertion_sort(data):
    N = len(data)
    for end_point in range(N):
        current_value = data[end_point]
        count = end_point
        while count > 0 and current_value <= data[count - 1]:
            # print '>>>', data, count, data[count], data[count - 1], data[count] > data[count - 1]
            data[count] = data[count - 1]
            count -= 1

        data[count] = current_value
        # print data, end_point, current_value
    return data
