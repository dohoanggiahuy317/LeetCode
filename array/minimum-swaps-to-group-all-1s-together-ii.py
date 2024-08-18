class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n1 = sum(nums)
        n = len(nums)
        if n1 == n:
            return 0
        
        nlist = nums + nums
        
        curr = n1 - sum(nlist[:n1])
        ans = curr

        for i in range(1, n):
            print(curr)
            if nlist[i-1] == 1:
                if nlist[i+n1-1] == 0:
                    curr += 1
                    ans = min(curr, ans)
            else:
                if nlist[i+n1-1] == 1:
                    curr -= 1
                    ans = min(curr, ans)

        return ans