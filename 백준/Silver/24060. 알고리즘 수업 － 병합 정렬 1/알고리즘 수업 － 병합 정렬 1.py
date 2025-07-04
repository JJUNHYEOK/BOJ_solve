import sys
sys.setrecursionlimit(2000000)

input = sys.stdin.readline

# 교훈
# 1. pseudo code를 준 문제는 그냥 그거 따라 풀자 .. 시간 복잡도 줄여도 구조가 다르면 어차피 오답 처리된다 ..
# 2. 들여쓰기에 조금 더 민감해지자. 한 라인이 어디에 있느냐에 따라 결과가 아예 달라짐
# 3. 여러 수를 입력받을때는 무조건 for나 map만 있는게 아니라 그냥 처음부터 list로 받아버리자
# 4. idx 값이 필요한 문제에서는 무조건 int형으로 반환할 수 있도록 하자(ㅋㅋ)

def merge_sort(arr, p, r):
  if p<r :
    q = (p+r) // 2 # 얘때문에 디버깅 20분 가량 소요됨 .. idx -> 무조건 integer임을 잊지 말자 ...
    merge_sort(arr, p, q)
    merge_sort(arr, q+1, r)
    merge(arr, p, q, r)

def merge(arr, p, q, r):
  global cnt, result

  i = p 
  j = q+1
  tmp = []

  while i<=q and j<=r:
    if arr[i] <= arr[j]:
      tmp.append(arr[i])
      i += 1

    else:
      tmp.append(arr[j])
      j += 1

  while i<=q:
    tmp.append(arr[i])
    i += 1

  while j<=r:
    tmp.append(arr[j])
    j += 1


  i = p
  t = 0

  while i<=r :
    arr[i] = tmp[t]
    cnt += 1

    if cnt == k:
      result = arr[i]
      break

    i += 1
    t += 1
    
n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
result = -1

merge_sort(arr, 0, n-1)

print(result)
