def countSumOfTwoRepresentations2(n, l, r):
    s = 0
    for i in range(l, r + 1):
        if i <= n - i <= r:
            s += 1
    return s
