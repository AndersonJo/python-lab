def binary_search(data, target):
    first = 0
    last = len(data)
    pos = -1

    while first <= last:
        midpoint = (first + last) / 2
        try:
            answer = data[midpoint]
        except IndexError:
            return -1

        if answer == target:
            pos = midpoint
            break

        if data[midpoint] >= target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return pos

