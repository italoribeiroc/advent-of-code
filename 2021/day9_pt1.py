def isLow(table, i, j):
    if -1 < i+1 < len(table) and table[i+1][j] <= table[i][j]:
        return False
    if -1 < j+1 < len(table[i]) and table[i][j+1] <= table[i][j]:
        return False
    if -1 < i-1 < len(table) and table[i-1][j] <= table[i][j]:
        return False
    if -1 < j-1 < len(table[i]) and table[i][j-1] <= table[i][j]:
        return False
    return True

with open('./2021/inp9.txt','r') as file:
    ans = 0
    table = file.read().split()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if isLow(table, i, j):
                print(table[i][j])
            ans += int(table[i][j]) + 1 if isLow(table, i, j) else 0
    print(ans)