class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        counter = 0
        today = 1

        while counter < n:
            if counter % 7 == 0 and counter > 0:
                today -= 6

            ans += today
            today += 1
            counter += 1
            
        return ans