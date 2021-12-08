with open('./2021/inp6.txt','r') as file:
    fishes = list(map(int, file.read().split(',')))
    for i in range(80):
        newFishes = fishes.count(0)
        fishes = list(map(lambda x : x - 1 if x > 0 else 6, fishes))
        fishes = fishes + [8] * newFishes
    print(len(fishes))