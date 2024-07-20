n = int(input())

bin = str(bin(n))[2:]

bin_reversed = bin[::-1]

dec = int(bin_reversed,2)

print(dec)