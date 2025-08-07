class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        def binsearch(arr, target):
            l, r = 0, len(arr) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m
                if arr[m] > target:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            return ans
        
        ans = inf
        MOD = 10 ** 9 + 7
        for supp in boxes:
            temp = 0
            d = True
            for pack in packages:
                ssupp = sorted(supp)
                idx = binsearch(ssupp, pack)
                if idx == -1:
                    d = False
                    break
                
                temp = (temp + (ssupp[idx] - pack) % MOD ) % MOD
            
            if d:
                ans = min(ans, temp)

        return -1 if ans == inf else ans