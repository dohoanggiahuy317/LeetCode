class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        curr = 0
        ans = 0

        for i in range(1, n+1):
            if i in set(banned):
                continue

            if curr + i > maxSum:
                break
            
            ans += 1
            curr += i

        return ans