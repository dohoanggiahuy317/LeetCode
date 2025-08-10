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

        def dfs(val, count):
            nonlocal n, d, visited, ans, MOD

            if val in visited:
                return

            if count == n:
                ans = (ans + 1) % MOD
                return

            # print(val)
            
            visited.add(val)

            for neigh in d[val]:
                dfs(neigh, count + 1)

        for val in nums:
            # print("STAT")
            visited = set()
            dfs(val, 1)

        return ans

        