class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        temp = 0
        nums.sort(reverse = True)
        curr = 0

        for x in nums:
            curr |= x

            temp += 1

            if curr > k:
                return temp

        return -1
