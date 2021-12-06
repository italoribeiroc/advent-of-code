def makeTable(fileName):
    with open(fileName, 'r') as file:
        size = 1000
        table = [['.' for j in range(size)] for i in range(size)]
        for line in file:
            start, end = line.split(' -> ')
            start, end = list(map(int, start.split(','))), list(map(int, end.split(',')))
            incX, incY = 1 if start[0] < end[0] else -1, 1 if start[1] < end[1] else -1
            while start[0] != end[0] or start[1] != end[1]:
                table[start[1]][start[0]] = 1 if table[start[1]][start[0]] == '.' else table[start[1]][start[0]] + 1
                start[0] += incX if start[0] != end[0] else 0
                start[1] += incY if start[1] != end[1] else 0
            else:
                table[start[1]][start[0]] = 1 if table[start[1]][start[0]] == '.' else table[start[1]][start[0]] + 1
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