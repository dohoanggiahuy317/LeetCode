class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pref = [0] * (len(nums) + 1)
        ans = 0
        left = 0

        for i, num in enumerate(nums):
            pref[i+1] = pref[i] + num

            while left <= i and k <= (i-left+1) * (pref[i+1]-pref[left]):
                left += 1
            ans += i-left + 1
            
        return ans