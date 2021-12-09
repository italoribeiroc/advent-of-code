with open('./2021/inp8.txt','r') as file:
    cnt = 0
    lights = [2, 3, 4, 7]
    for line in file:
        output = line.split('|')[1].split()
        for digit in output:
            cnt += 1 if len(digit) in lights else 0
    print(cnt)