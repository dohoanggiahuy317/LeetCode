class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        MOD = 10 ** 9 + 7

        while n > 0:
            power = int(math.log(n, 2))
            powers.append(2 ** power)
            n -= 2 ** power

        powers.sort()
        pref_prod = [1]
        curr_prod = 1
        for power in powers:
            curr_prod = (curr_prod * power) 
            pref_prod.append(curr_prod)        

        ans = []
        for l, r in queries:
            ans.append((pref_prod[r+1]//pref_prod[l])% MOD)

        return ans