class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        triplet = 0

        for j in range(n):
            count_i_k = 0
            
            for i_k in range(n):  
                if i_k != j and abs(nums[j] - nums[i_k]) == diff:
                   count_i_k += 1
            
            if count_i_k == 2:
                triplet += 1

        return triplet
