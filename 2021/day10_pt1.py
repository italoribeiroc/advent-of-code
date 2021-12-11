def bracketValue(bracket):
    if bracket == ')':
        return 3
    elif bracket == ']':
        return 57
    elif bracket == '}':
        return 1197
    elif bracket == '>':
        return 25137
    print(bracket)

with open('./2021/inp10.txt','r') as file:
    ans = 0
    lines = file.read().split('\n')
    for line in lines:
        stack = []
        for bracket in line:
            if bracket == '(':
                stack.append(')')
            elif bracket == '[':
                stack.append(']')
            elif bracket == '{':
                stack.append('}')
            elif bracket == '<':
                stack.append('>')
            else:
                if bracket == stack[-1]:
                    stack.pop()
                else:
                    ans += bracketValue(bracket)
                    break
    print(ans)
