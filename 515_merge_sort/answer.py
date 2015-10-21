# [54, 26, 93, 17, 77, 31, 44, 55, 20]
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) / 2
        left, right = data[:mid], data[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

    return data
