import sys

input = sys.stdin.readline

while True:
    stk = []
    string = input().rstrip()
    flag = 0

    if string == '.':
            break

    for word in string:
        if word == '(' or word == '[':
            stk.append(word)

        elif word == ')':
            if not stk or stk[-1] != '(':
                flag = 1
                break
            stk.pop()
        
        elif word == ']':
            if not stk or stk[-1] != '[':
                flag = 1
                break
            stk.pop()

    if not stk and flag == 0:
        print('yes')
    
    else:
        print('no')