result = []

while True:

    a, b, c = map(int,input().split())

    if a == 0 and b == 0 and c == 0:
        break
      

    num = [a,b,c]
    num.sort()


    if num[0]**2 +num[1]**2 == num[2]**2:
        result.append('right')

    else:
        result.append('wrong')


for i in range(len(result)):
    print(result[i])
    
