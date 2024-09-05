class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums:
            return []
        s = 0

        ans = []

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if i > s + 1:
                    ans.append(str(nums[s]) + "->" + str(nums[i-1]) )
                elif i == s + 1:
                    ans.append(str(nums[s]))

                s = i

        if s < len(nums) - 1:
            ans.append(str(nums[s]) + "->" + str(nums[-1]) )
        else:
            ans.append(str(nums[s]))

        return ans