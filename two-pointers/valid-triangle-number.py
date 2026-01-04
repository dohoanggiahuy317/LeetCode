class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sort array and initialize count as 0
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(0, n-2):
            k = i + 2
            for j in range(i + 1, n):
                while (k < n and nums[i] + nums[j] > nums[k]):
                    k += 1
                if(k>j):
                    count += k - j - 1
        return count
 