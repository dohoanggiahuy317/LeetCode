class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        n = len(nums)
        nums.sort()

        for x in range(0, 2**n):
            bin_x = bin(x)[2:]
            bin_x = (n - len(bin_x))*"0" + bin_x

            sub = []
            for bit_ind in range(n):
                if bin_x[bit_ind] == "1":
                    sub.append(nums[bit_ind])

            subset.append(sub[:]) if sub[:] not in subset else None
        
        return subset