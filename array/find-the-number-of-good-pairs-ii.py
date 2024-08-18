class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        div = defaultdict(int)

        for num in nums1:
            for d in range(1, int(num**0.5) + 1):
                if num % d == 0:
                    if d % k == 0:
                        div[d] += 1
                    if (num // d) % k == 0 and d != num // d:
                        div[num // d] += 1

        ans = 0
        for num in nums2:
            if num * k in div:
                ans += div[num * k]

        return ans

        
        