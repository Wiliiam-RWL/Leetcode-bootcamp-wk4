from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = deque()
        min_len = float('inf')
        for item in nums:
            que.append(item)
            if sum(que) >= k:
                while sum(que) - que[0] >= k:
                    que.popleft()
                if len(que) < min_len:
                    min_len = len(que)
                que.popleft()
            while que and que[0] <= 0:
                que.popleft()
                if sum(que) >= k:
                    while sum(que) - que[0] >= k:
                        que.popleft()
                    if len(que) < min_len:
                        min_len = len(que)
                    que.popleft()
        return -1

'''
len = 1: no other way O(n)

sum(A[1,..,2]) = sum(A[1,1] + A[2])

sum(i, j) = sum(i, j-1) + A[j], if j - i > 1

for loop 1,

for i = 2 to A.length:
    for index = 1 to A.length - i

O(n^2)

=================
que = deque()

for item in A:

'''