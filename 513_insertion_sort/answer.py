def insertion_sort(data):
    for end in range(1, len(data)):
        end_value = data[end]
        count = end
        while count > 0 and data[count - 1] >= end_value:
            data[count] = data[count-1]
            count -= 1
        data[count] = end_value
    return data
