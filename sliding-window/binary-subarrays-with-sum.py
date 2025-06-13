class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = 0
        nums += [1]
        freq = defaultdict(int)
        ans = 0

        for i, num in enumerate(nums):
            print(freq)
            if num == 1:
                pref += 1
                freq[pref] = i

                if pref-1-goal >= 0:
                    right_pad = freq[pref]
                    right = freq[pref-1]
                    left = freq[pref-goal]
                    left_pad = freq[pref-1-goal]
                    # print("yp")
                    # print(pref, dict(freq))
                    # print(left_pad, left, right, right_pad)
                    # print()

                    if left > right:
                        ans += right_pad * (right_pad + 1) // 2
                    else:
                        ans += (right_pad - right) * ((left - left_pad) * int(left != left_pad) + 1 * int(left == left_pad))


                    


        return ans