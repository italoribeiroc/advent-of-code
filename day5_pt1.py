def makeTable(fileName):
    with open(fileName, 'r') as file:
        size = 1000
        table = [['.' for j in range(size)] for i in range(size)]
        for line in file:
            start, end = line.split(' -> ')
            start, end = list(map(int, start.split(','))), list(map(int, end.split(',')))
            if start[0] == end[0]:
                for i in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    table[i][start[0]] = 1 if table[i][start[0]] == '.' else table[i][start[0]] + 1
            if start[1] == end[1]:
                for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                    table[start[1]][i] = 1 if table[start[1]][i] == '.' else table[start[1]][i] + 1
    return table


def main():
    table = makeTable("inp5.txt")
    cont = 0
    for line in table:
        for num in line:
            if num != '.' and num >= 2:
                cont += 1
    print(cont)
main()