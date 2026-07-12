class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()

        n = len(coins)
        starts = [l for l, r, c in coins]
        ends = [r for l, r, c in coins]

        pref = [0] * (n + 1)

        for i, (l, r, c) in enumerate(coins):
            pref[i + 1] = pref[i] + (r - l + 1) * c

        def cal_coins(x):
            lb, rb = 0, n - 1
            idx = n
            while lb <= rb:
                mb = (lb + rb) // 2
                if x <= coins[mb][1]:
                    idx = mb
                    rb = mb - 1
                else:
                    lb = mb + 1
            
            total = pref[idx]

            if idx < n:
                l, r, c = coins[idx]
                if l <= x <= r:
                    total += (x - l + 1) * c

            return total

        ans = 0

        for l, r, c in coins:
            lw = l
            rw = l + k - 1
            ans = max(ans, cal_coins(rw) - cal_coins(lw - 1))

            rw = r
            lw = r - k + 1
            ans = max(ans, cal_coins(rw) - cal_coins(lw - 1))

        return ans