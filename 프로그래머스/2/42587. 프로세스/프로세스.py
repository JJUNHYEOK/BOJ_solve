from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    ans = 0

    while queue:
        cur = queue.popleft()

        if any(cur[1] < item[1] for item in queue):
            queue.append(cur)

        else:
            ans += 1

            if cur[0] == location:
                return ans