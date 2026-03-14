a, b = map(int,input().split())
c, d = map(int,input().split())

hanyang = a + c
yongdap = b + d

if hanyang < yongdap:
    print('Hanyang Univ.')

elif hanyang == yongdap:
    print('Either')

else:
    print('Yongdap')