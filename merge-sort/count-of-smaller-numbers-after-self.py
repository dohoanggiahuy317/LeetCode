class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = SortedList()
        ans = []

        for i, num in enumerate(reversed(nums)):
            
            idx = bisect_left(seen, num)
            ans.append(idx)
            seen.add(num)

        return ans[::-1]
