def sequence(d):
    j = [0 for i in range(len(d))]
    d[0], j[0] = 0, 0
    k, j[1] = 1, 1
    for i in range(2, len(d)):
        r = k
        while d[j[r]] > max(d[i], r):
            r -= 1
        if d[i] > r:
            for m in range(k, r, -1):
                j[m + 1] = j[m]
            j[r + 1] = i
            k = k + 1
    return k, j

#   [0  1   2   3   4   5   6]
g = [0, 20, 15, 10, 7,  5,  3]
d = [0, 3,  1,  1,  4,  2,  3]

k, j = sequence(d)
print(f'Number of tasks: {k}\nOrder of tasks: {d}')
for i in j:
    print(f'{g[i]}\t', end=',')
print()
for i in j:
    print(f'{d[i]}\t', end=',')
