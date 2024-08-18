class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        dp = [rev(x) for x in nums]
        track = {}

        for x, y in zip(nums, dp):
            diff = x - y

            if diff in track:
                track[diff] += 1
            else:
                track[diff] = 1
        
        ans = 0

        for m, n in track.items():
            if n > 0:
                ans += (n * (n - 1)) // 2
                ans = ans % (10 ** 9 + 7)

        return ans % (10 ** 9 + 7)