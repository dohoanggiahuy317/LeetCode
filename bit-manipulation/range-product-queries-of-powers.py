class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        exps = []
    
        while n > 0:
            exp = int(math.log(n, 2))
            exps.append(exp)
            n -= 2 ** exp

        exps.sort()
        prefsum = [0]
        for exp in exps:
            new_pref = (prefsum[-1] + exp) 
            prefsum.append(new_pref)        

        ans = []
        for l, r in queries:
            ans.append((1 << (prefsum[r+1] - prefsum[l])) % MOD)

        return ans