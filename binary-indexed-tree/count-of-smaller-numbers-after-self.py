class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = SortedList()
        ans = [0] * n

        for i, num in enumerate(reversed(nums)):
            
            idx = bisect_left(seen, num)
            ans[-i - 1] = idx
            seen.add(num)

        return ans
