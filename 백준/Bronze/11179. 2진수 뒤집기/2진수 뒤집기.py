n = int(input())

bin = str(bin(n))[2:]

bin_reversed = bin[::-1]

dec = int(bin_reversed,2)

print(dec)


--------------------------------------------

[clean code]
import sys
n = int(sys.stdin.readline())
print(int(bin(n)[2:][::-1],2))
