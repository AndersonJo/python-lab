def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    check = list(s2)
    correct = True
    for c in s1:
        pos = 0
        found = False
        for i in range(len(s2)):
            if c == check[i]:
                found = True
                pos = i
        if found:
            check[pos] = None
        else:
            correct = False
    return correct
