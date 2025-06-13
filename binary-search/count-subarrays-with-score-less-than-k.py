class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pref = [0] * (len(nums) + 1)
        ans = 0

        for i, num in enumerate(nums):
            pref[i+1] = pref[i] + num
            l = 1

            while i+1-l >= 0 and k > l * (pref[i+1]-pref[i+1-l]):
                # print(l, pref[i+1-l], pref[i+1])
                ans += 1
                l += 1
            # print(pref)
            # print()
            
        return ans