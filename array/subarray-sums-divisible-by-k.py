class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prods = {}
        prefix = ans = 0
        for num in nums:
            prefix += num
            mod = prefix%k
            if mod in prods:
                ans += prods[mod]
                prods[mod] += 1
            else:
                prods[mod] = 1
        return ans+(prods[0] if 0 in prods else 0)