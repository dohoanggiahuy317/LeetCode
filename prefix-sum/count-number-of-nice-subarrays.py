class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: -1, {0: -1})
        ans = 0
        pref = 0
        # nums += [1]

        for i, num in enumerate(nums):
            if num % 2 == 1:
                pref += 1
                freq[pref] = i
            
            ans += freq[pref-k+1] - freq[pref-k]
            # print(pref, dict(freq), ans)



        return ans