class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
        n = len(nums)
        MOD = 10**9 + 7
        d = defaultdict(list)

        for a in nums:
            for b in nums:
                if a != b and (a % b == 0 or b % a == 0):
                    d[a].append(b)

        ans = 0
        temp = []

        def backtrack(val):
            nonlocal ans
            if val in temp:
                return

            temp.append(val)

            if len(temp) == n:
                ans = (ans + 1) % MOD
            else:
                for nxt in d[val]:
                    backtrack(nxt)

            temp.pop()

        for val in nums:
            backtrack(val)

        return ans

        