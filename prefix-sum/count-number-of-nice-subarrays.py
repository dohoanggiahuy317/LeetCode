class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int, {0: -1})
        ans = 0
        pref = 0
        nums += [1]

        for i, num in enumerate(nums):
            if num % 2 == 1:
                pref += 1
                freq[pref] = i

                if pref-k-1 >= 0:
                    right_pad = freq[pref]
                    right = freq[pref-1]
                    left = freq[pref-k]
                    left_pad = freq[pref-k-1]
                
                    if left > right:
                            ans += (right_pad-right) * (right_pad-right - 1) // 2
                    else:
                        ans += (right_pad - right) * ((left - left_pad) * int(left != left_pad) + 1 * int(left == left_pad))

        return ans