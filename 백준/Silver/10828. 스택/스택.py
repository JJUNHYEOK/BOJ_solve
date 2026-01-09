import sys

input = sys.stdin.readline

n = int(input())
stk = []

for _ in range(n):  
    jdg = input().split() 
    cmd = jdg[0]

    if cmd == 'push':
        stk.append(int(jdg[1]))

    elif cmd == 'pop':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif cmd == 'size':
        print(len(stk))

    elif cmd == 'empty':
        if not stk:
            print(1)
        else:
            print(0)

    elif cmd == 'top':
        if stk:
            print(stk[-1])
        else:
            print(-1)