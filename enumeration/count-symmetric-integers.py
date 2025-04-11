class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            if len(str(i)) % 2 == 1:
                continue
            n =  len(str(i)) // 2
            ans += 1 if sum(list(map(int, list(str(i)[:n])))) == sum(list(map(int, list(str(i)[n:])))) else 0
        
        return ans