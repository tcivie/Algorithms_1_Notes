def knapSack(W, wt, val):
    n = len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Calculate the matrix
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                table[i][j] = max(val[i - 1] + table[i - 1][j - wt[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]
    # Traverse back the results
    results = []
    i = n
    j = W
    while True:
        if table[i][j] == table[i - 1][j]:
            results.append(i - 2)
            i -= 2
        else:
            results.append(i - 1)
            j -= wt[i - 1]  # Move back the weight
            i -= 1
        if table[i][j] == 0:  # Do while
            break
    return results


val = [50,100,150,200]
wt = [8,16,32,40]
W = 64

print(knapSack(W, wt, val))
