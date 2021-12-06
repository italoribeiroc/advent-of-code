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

def main():
    sortNums, tables = process_data("inp4.txt")
    for num in sortNums:
        for table in tables:
            table = findNum(table, num)
            if itWon(table):
                print(table)
                print(unmarked(table),"*", num, "=", unmarked(table) * num)
                return

main()

