def totalScore(stack):
    stack = stack[::-1]
    score = 0
    for bracket in stack:
        score *= 5
        if bracket == ')':
            score += 1
        elif bracket == ']':
            score += 2
        elif bracket == '}':
            score += 3
        elif bracket == '>':
            score += 4
    return score

with open('./2021/inp10.txt','r') as file:
    ans = []
    lines = file.read().split('\n')
    for line in lines:
        stack = []
        lenLine = len(line)
        for i in range(lenLine):
            if line[i] == '(':
                stack.append(')')
            elif line[i] == '[':
                stack.append(']')
            elif line[i] == '{':
                stack.append('}')
            elif line[i] == '<':
                stack.append('>')
            else:
                if line[i] == stack[-1]:
                    stack.pop()
                else:
                    break
            if i == lenLine - 1:
                ans.append(totalScore(stack))
    ans.sort()
    print(ans[len(ans) // 2])
