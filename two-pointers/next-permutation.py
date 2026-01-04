import copy

class Solution:
    
    def changeNums(self, nums1, nums2):
        for i in range(len(nums2)):
            nums1[i] = nums2[i]
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnums = copy.deepcopy(nums)
        
        n = len(cnums)
        split = -1
        
        for i in range(n-1):
            start = n - 1 - i
            if cnums[start] <= cnums[start - 1]:
                continue
            else:
                split = start
                break
        
        if split == -1:
            snums = sorted(cnums)
            self.changeNums(nums, snums)
            return
                
        fi = cnums[:start]
        la = cnums[start:]
        la.sort()

        for i in range(len(la)):
            if la[i] > fi[-1]:
                fi[-1], la[i] = la[i], fi[-1]
                break
        
        fnums = fi+la
        self.changeNums(nums, fnums)
        
        
            