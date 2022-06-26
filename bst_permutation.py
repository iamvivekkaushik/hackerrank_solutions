#
def numberOfBST(n):
    if n == 0:
        return 0
    
    list = [0] * (n+1)

    list[0], list[1] = 1, 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            list[i] += list[j-1] * list[i-j]
    
    return list[n]

print(numberOfBST(5))
