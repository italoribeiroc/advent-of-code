with open("inp3.txt", "r") as file:
    binNums = file.read().split("\n")
    gamma, epsilon = '', ''
    for i in range(len(binNums[0])):
        one, zeros = 0, 0
        for j in range(len(binNums)):
            one += 1 if binNums[j][i] == '1' else 0
            zeros += 1 if binNums[j][i] == '0' else 0
        gamma += '1' if one > zeros else '0'
        epsilon += '0' if one > zeros else '1'
    print(gamma, epsilon)
    print(int(gamma, 2) * int(epsilon, 2))