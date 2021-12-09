def transfSet(num):
    return set([letter for letter in num])

with open('./2021/inp8.txt','r') as file:
    ans = 0
    for line in file:
        aux = line.split('|')
        algs, output = aux[0].split(), aux[1].split()
        algs.sort(key = lambda x : len(x))
        nums = { 1: transfSet(algs[0]), 7: transfSet(algs[1]), 4: transfSet(algs[2]), 8: transfSet(algs[-1]) }
        strOutput = ""
        for value in output:
            num = transfSet(value)
            lenNum = len(num)
            if lenNum == 2:
                strOutput += '1'
            elif lenNum == 3:
                strOutput += '7'
            elif lenNum == 4:
                strOutput += '4'
            elif lenNum == 7:
                strOutput += '8'
            elif lenNum == 5 and len(num & nums[7]) == 3:
                strOutput += '3'
            elif lenNum == 5 and len(num & nums[4]) == 2:
                strOutput += '2'
            elif lenNum == 5 and len(num & nums[4]) == 3 and len(num & nums[1]) == 1:
                strOutput += '5'
            elif lenNum == 6 and len(num & nums[4]) == 3 and len(num & nums[1]) == 2:
                strOutput += '0'
            elif lenNum == 6 and len(num & nums[4]) == 3 and len(num & nums[1]) == 1:
                strOutput += '6'
            elif lenNum == 6 and len(num & nums[4]) == 4:
                strOutput += '9'
        ans += int(strOutput)
        print(strOutput)
            

    print(ans)