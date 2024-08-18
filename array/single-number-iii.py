class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)

        return list(s)