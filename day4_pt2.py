def process_data(fileName):
    with open(fileName, 'r') as file:
        nums = list(map(int, file.readline().split(',')))
        tables = []
        table = []
        for line in file:
            if line == "\n":
                continue
            table.append(list(map(int, line.split())))
            if len(table) >= 5:
                tables.append(table)
                table = []
    return nums, tables

def findNum(table, target):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == target:
                table[i][j] = table[i][j] * -1 if table[i][j] else -1

    return table

def unmarked(table):
    soma = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] >= 0:
                soma += table[i][j]
    return soma

def itWon(table):
    for i in range(len(table)):
        cnt = 0
        for j in range(len(table[i])):
            if table[i][j] < 0:
                cnt += 1
            if cnt == 5:
                return True

    for i in range(len(table[0])):
        cnt = 0
        for j in range(len(table)):
            if table[j][i] < 0:
                cnt += 1
            if cnt == 5:
                return True
    return False

def printTable(table):
    for line in table:
        print(*line)
    print()

def main():
    sortNums, tables = process_data("inp4.txt")
    wonTables = [0 for i in range(len(tables))]
    for num in sortNums:
        for i in range(len(tables)):
            tables[i] = findNum(tables[i], num)
            if itWon(tables[i]):
                wonTables[i] = 1
            if sum(wonTables) == len(tables):
                printTable(tables[i])
                print(unmarked(tables[i]),"*", num, "=", unmarked(tables[i]) * num)
                return

main()