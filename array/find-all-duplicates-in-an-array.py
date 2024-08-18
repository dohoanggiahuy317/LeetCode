class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = set()
        ans = []
        for x in nums:
            if x in d:
                ans.append(x)
            else:
                d.add(x)

        return ans 
        