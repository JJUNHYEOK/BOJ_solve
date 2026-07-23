def solution(clothes):
    ans = 1
    hash = {}

    for name, category in clothes:
        hash[category] = hash.get(category, 0) + 1

    for cnt in hash.values():
        ans *= (cnt+1)

    return ans - 1