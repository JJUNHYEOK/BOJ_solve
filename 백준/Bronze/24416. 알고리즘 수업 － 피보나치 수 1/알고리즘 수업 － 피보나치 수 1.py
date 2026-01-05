import sys

input = sys.stdin.readline

def fib(n):
    mem = [0]*(n+1)
    mem[1] = mem[2] = 1

    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2]

    return mem[i]
 
def fibonacci(n):
    return n-2

n = int(input())

print(fib(n), fibonacci(n))
