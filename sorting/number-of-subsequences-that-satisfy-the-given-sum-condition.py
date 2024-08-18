class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        s = 0
        e = len(nums) - 1
        mod = 10 ** 9 + 7
        ans = 0

        while s <= e:
            if nums[s] + nums[e] > target:
                e -= 1

            else:
                ans += pow(2, e - s, mod)
                s += 1
        
        return ans % mod