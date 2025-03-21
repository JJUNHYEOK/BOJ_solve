t = int(input())

for _ in range(t):
    par = input()
    stack = []

    for i in par:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:  
                print("NO")
                break
            stack.pop()
    else:
        if stack: 
            print("NO")
        else:
            print("YES")
