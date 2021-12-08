from collections import defaultdict

with open('./2021/inp6.txt','r') as file:
    fishes = list(map(int, file.read().split(',')))
    delta = 7  
    delta0 = 9 
    births = defaultdict(lambda: 0)
    population = len(fishes)
    for d in fishes:
        births[d + 1] += 1

    for day in range(1, 256 + 1):
        birth_count = births[day]
        if birth_count > 0:
            population = population + birth_count
            births[day + delta] += birth_count
            births[day + delta0] += birth_count
    print(population)