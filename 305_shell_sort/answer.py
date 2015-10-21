def shell_sort(data):
    N = len(data)
    sub_count = N / 2
    while sub_count > 0:
        gap_insertion_sort(data, sub_count)
        sub_count /= 2
    return data


def gap_insertion_sort(data, gap):
    N = len(data)
    for end_point in range(gap, N, gap):
        current_value = data[end_point]
        position = end_point

        while position - gap >= 0 and data[position - gap] > current_value:
            data[position] = data[position - gap]
            position -= gap

        data[position] = current_value
        # print data, 'position:%d current_value:%d, end_point:%d' % (position, current_value, end_point)
