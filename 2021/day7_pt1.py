import numpy as np

with open('./2021/inp7.txt','r') as file:
    crabs = list(map(int, file.read().split(',')))
    lessFuel = np.median(crabs)
    totalFuel = 0
    for crab in crabs:
        totalFuel += abs(crab - lessFuel)
    print(totalFuel)
