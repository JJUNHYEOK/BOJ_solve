n = int(input())
list = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    list.append((age,name))


list.sort(key = lambda x: x[0])

for i in list:
    print(i[0], i[1])

