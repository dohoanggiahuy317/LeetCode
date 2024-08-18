class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_total(li):
            ans = 0
            for x in li:
                ans = ans ^ x
            return ans

        n = len(nums)
        ans = 0

        for i in range(2 ** n):
            bin_i = bin(i)[2:]
            bin_i = "0" * (n - len(bin_i)) + bin_i
            new_li = []


            for j in range(len(bin_i)):
                if bin_i[j] == "1":
                    new_li.append(nums[j])

            ans += xor_total(new_li)

            #print(new_li)

        return ans