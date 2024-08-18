class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        chosen = [0] * n
        ans = []
        subset = []

        def search():
            if len(subset) == n:
                ans.append(subset[:])
                return
            else:
                for i in range(n):
                    if chosen[i] == 1:
                        continue
                    chosen[i] = 1
                    subset.append(nums[i])
                    search()

                    chosen[i] = 0
                    subset.pop()

        search()
        return ans