def filtrate(nums, bine, pos):
    filt = []
    for num in nums:
        if num[pos] == bine:
            filt.append(num)
    return filt

def findRating(aux, typo):
    for i in range(len(aux[0])):
        one, zeros = 0, 0
        for j in range(len(aux)):
            one += 1 if aux[j][i] == '1' else 0
            zeros += 1 if aux[j][i] == '0' else 0
        if len(aux) > 1:
            if typo == 'O':
                aux = filtrate(aux, '1' if one >= zeros else '0', i)
            elif typo == "CO2":
                aux = filtrate(aux, '0' if one >= zeros else '1', i)
        else:
            break
    return aux[0]

with open("inp3.txt", "r") as file:
    binNums = file.read().split("\n")
    auxO, auxCO2 = findRating(binNums, "O"), findRating(binNums, "CO2")
    
    print(auxO, auxCO2)
    print(int(auxO, 2) * int(auxCO2, 2))