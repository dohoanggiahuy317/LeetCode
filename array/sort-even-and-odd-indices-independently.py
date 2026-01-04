class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(0, len(nums), 2):
            even.append(nums[i])
        for i in range(1, len(nums), 2):
            odd.append(nums[i])
            
        even.sort()
        odd.sort(reverse = True)
        
        for i in range(0, len(nums), 2):
            nums[i] = even[int(i/2)]
        for i in range(1, len(nums), 2):
            nums[i] = odd[int(i/2)]
        
        return nums