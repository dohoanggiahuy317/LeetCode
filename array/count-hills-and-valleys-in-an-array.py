class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        redu = []
        for num in nums:
            if redu and num == redu[-1]:
                continue
            redu.append(num)

        ans = 0
        for i in range(1, len(redu) - 1):
            # print(redu[i-1], redu[i], redu[i+1])
            if redu[i-1] < redu[i] > redu[i+1] or redu[i-1] > redu[i] < redu[i+1]:
                ans += 1
        
        return ans