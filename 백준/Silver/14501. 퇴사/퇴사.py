import sys

input = sys.stdin.readline

n = int(input())
time = []
price = []

for _ in range(1,n+1):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)

def solution(arr1, arr2):

    dp = [0]*(n+1)

    for i in range(n-1, -1, -1):

        jump = dp[i+1]

        if i+arr1[i] <= n:
            do = arr2[i]+dp[i+arr1[i]]
            dp[i] = max(do, jump)

        else:
            dp[i] = jump

    return dp[0]


print(solution(time, price))