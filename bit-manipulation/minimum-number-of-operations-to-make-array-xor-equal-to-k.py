class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        num = nums.pop()
        curr = bin(num)[2:]
        curr = '0' * (20 - len(curr)) + curr

        for num in nums:
            bnum = bin(num)[2:]
            bnum = '0' * (20 - len(bnum)) + bnum

            new_curr = ""
            for i in range(20):
                if curr[i] == bnum[i]:
                    new_curr += '0'
                else:
                    new_curr += "1"
            
            curr = new_curr[:]

        bk = bin(k)[2:]
        bk = '0' * (20 - len(bk)) + bk

        ans = 0

        for i in range(20):
            if curr[i] != bk[i]:
                ans += 1

        return ans