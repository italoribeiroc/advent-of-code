import numpy as np

with open('./2021/inp7.txt','r') as file:
    crabs = list(map(int, file.read().split(',')))
    lessFuel = int(np.mean(crabs))
    totalFuel = 0
    for crab in crabs:
        for i in range(1, abs(crab - lessFuel) + 1):
            totalFuel += i
    print(lessFuel, totalFuel)
