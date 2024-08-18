class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for i in range(2**len(nums)):
            bin_i = bin(i)[2:]
            bin_i = "0" * (len(nums) - len(bin_i)) + bin_i

            temp = []

            for j in range(len(nums)):
                if bin_i[j] == "1":
                    temp.append(nums[j])

            ans.append(temp)

        return ans