class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = {}

        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                if diagonal in d:
                    d[diagonal].append(nums[row][col])
                else:
                    d[diagonal] = [nums[row][col]]

        ans = []

        for i in range(len(d)):
            ans.extend(d[i])

        return ans