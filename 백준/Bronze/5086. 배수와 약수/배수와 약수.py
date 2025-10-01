a, b = 1, 1
result = []

while True:
    a, b = map(int,input().split())

    if a == 0 and b == 0:
        break

    if a%b == 0:
        result.append('multiple')
    elif b%a == 0:
        result.append('factor')
    else:
        result.append('neither')


for status in result:
    print(status)

    