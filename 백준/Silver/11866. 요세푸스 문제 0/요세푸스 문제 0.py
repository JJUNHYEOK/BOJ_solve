n, k = map(int,(input().split()))
cir = []
result = []
idx = 0

for i in range(1, n+1):
    cir.append(i)

def josephus(k):
    while len(cir) > 0:
        global idx
        idx = (idx + k - 1)%len(cir)
        result.append(cir.pop(idx))

        
    return result

josephus(k)

print(f"<{', '.join(map(str,result))}>")
