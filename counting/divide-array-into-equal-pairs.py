from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = Counter()

        for num in nums:
            d[num] += 1

        for u, v in d.items():
            if v % 2 == 1:
                return False

        return True