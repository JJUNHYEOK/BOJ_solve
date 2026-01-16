import sys

input = sys.stdin.readline

n = int(input())
nums = []
a = 0

for _ in range(n):
    nums.append(int(input()))

for num in nums:
    a += num

mean =(round(a/len(nums)))
sorting = sorted(nums)
median = sorting[len(nums)//2]

print(mean)
print(median)

dic = dict()

for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxi = max(dic.values())
maxi_dic = [k for k, v in dic.items() if v == maxi]

maxi_dic.sort()

if len(maxi_dic) > 1:
    print(maxi_dic[1])
else:
    print(maxi_dic[0])

print(max(nums)-min(nums))