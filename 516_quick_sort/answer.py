def quick_sort(data):
    less = []
    equal = []
    more = []

    if len(data) > 1:
        pivot = data[0]

        for v in data:
            if v < pivot:
                less.append(v)
            elif v == pivot:
                equal.append(v)
            elif v > pivot:
                more.append(v)

        return quick_sort(less) + equal + quick_sort(more)
    return data
