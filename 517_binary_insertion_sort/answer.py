def binary_insertion_sort(data):
    for i in xrange(1, len(data)):
        if data[i - 1] < data[i]:
            continue

        left = 0
        right = i
        while left < right:
            mid = (left + right) / 2

            if data[i] > data[mid]:
                left = mid + 1
            else:
                right = mid

        j = i
        while j > left:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1
    return data
