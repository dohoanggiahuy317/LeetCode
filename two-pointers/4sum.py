class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()

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
                        quad = tuple(sorted([nums[a], nums[b], nums[c], nums[d]]))
                        if quad not in ans:
                            ans.add(quad)
                        c += 1
                        d -= 1

        return [list(quad) for quad in ans]
                    