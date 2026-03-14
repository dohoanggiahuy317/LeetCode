class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        cur_sum = 0 # Tổng từ số đầu tiên đến số thứ i
        
        for i, num in enumerate(nums):
            curr_sum += num
            arr[i] = curr_sum
        
        return arr