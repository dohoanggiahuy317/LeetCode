class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = defaultdict(int)
        right_sum = defaultdict(int)

        for i in range(n):
            left_sum[i] = left_sum[i - 1] + nums[i]
        
        for i in range(n-1, -1, -1):
            right_sum[i] = right_sum[i + 1] + nums[i]
        
        for i in range(n):
            if left_sum[i - 1] == right_sum[i + 1]:
                return i 

        return -1
