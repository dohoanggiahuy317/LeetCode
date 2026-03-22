class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for a in range(n):
            for b in range(a + 1, n):
                
                c = b + 1
                d = n - 1
                while c < d:
                    if nums[a] + nums[b] + nums[c] + nums[d] > target:
                        d -= 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        c += 1
                    else:
                        if not (
                            ans and 
                            all(x == y for x, y in zip(ans[-1], [nums[a], nums[b], nums[c], nums[d]]))
                            ):
                            ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1

        return ans
                    