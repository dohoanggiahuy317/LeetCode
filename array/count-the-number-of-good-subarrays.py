from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        d = Counter()
        start, end = 0, 0
        d[nums[0]] += 1
        curr = 0
        ans = 0

        while True:
            # print(nums[start:end+1], curr, ans)
            if curr < k:
                if end == len(nums) - 1:
                    break
                end = min(end + 1, len(nums) - 1)
                d[nums[end]] += 1
                curr += d[nums[end]] - 1
            elif curr >= k:
                start += 1
                d[nums[start-1]] -= 1
                curr -= d[nums[start - 1]]
                ans += len(nums) - end

        return ans




