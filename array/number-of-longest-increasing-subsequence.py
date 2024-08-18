class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp_l = {0:1}
        dp_c = {0:1}


        for i in range(1, len(nums)):
            curr_c = 1
            curr_l = 1

            for j in range(i-1, -1 , -1):
                if nums[j] < nums[i]:
                    if dp_l[j] + 1 > curr_l:
                        curr_l = dp_l[j] + 1
                        curr_c = 0

                    if dp_l[j] + 1 == curr_l:
                        curr_c += dp_c[j]

            dp_c[i] = curr_c
            dp_l[i] = curr_l


        curr_max = 0
        ans = 0
        for i in range(len(nums)):
            if dp_l[i] > curr_max:
                curr_max = dp_l[i]
                ans = 0
            if curr_max == dp_l[i]:
                ans += dp_c[i]

        return ans

            