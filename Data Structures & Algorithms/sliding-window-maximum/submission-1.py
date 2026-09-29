class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            windowLen = r - l + 1
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if windowLen == k:
                res.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1
        return res