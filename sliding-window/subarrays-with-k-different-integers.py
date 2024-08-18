class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(nums, k):
            ans, count, l = 0, 0, 0
            d = Counter()

            for r in range(0, len(nums)):
                new_num = nums[r]
                d[new_num] += 1

                if d[new_num] == 1:
                    count += 1
                
                while count > k:
                    rev_num = nums[l]
                    d[rev_num] -= 1
                    l += 1
                    if d[rev_num] == 0:
                        count -= 1
                
                ans += r - l + 1

            return ans

        return solve(nums, k) - solve(nums, k - 1)