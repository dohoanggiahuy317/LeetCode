class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        temp = []

        for i in range(n):
            curr = nums[i]
            temp.append(curr)

            for j in range(i + 1, n):
                curr += nums[j]
                temp.append(curr)

        temp.sort()

        return sum(temp[left-1: right]) % (10**9 + 7)