class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        freq = defaultdict(int, {0: 1})
        ans = 0
        pref = 0

        for i, num in enumerate(nums):
            pref += num
            ans += freq[pref-goal]
            freq[pref] += 1
                
        return ans

        # pref = 0
        # nums += [1]
        # freq = defaultdict(int, {0:-1})
        # ans = 0

        # for i, num in enumerate(nums):
        #     if num == 1:
        #         pref += 1
        #         freq[pref] = i

        #         if pref-1-goal >= 0:
        #             right_pad = freq[pref]
        #             right = freq[pref-1]
        #             left = freq[pref-goal]
        #             left_pad = freq[pref-1-goal]

        #             if left > right:
        #                 ans += (right_pad-right) * (right_pad-right - 1) // 2
        #             else:
        #                 ans += (right_pad - right) * ((left - left_pad) * int(left != left_pad) + 1 * int(left == left_pad))


                    


        # return ans