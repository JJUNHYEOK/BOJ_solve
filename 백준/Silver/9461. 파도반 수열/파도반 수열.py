import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    dp = [0]*(num+1)


    for i in range(1, num+1):
        
        if i <= 3:
            dp[i] = 1

        else:
            dp[i] = dp[i-3] + dp[i-2]

    print(dp[-1])