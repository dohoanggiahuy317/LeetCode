class Solution:
    def knightDialer(self, n: int) -> int:
        m = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        @cache
        def dfs(s, i):
            nonlocal n, m
            if i == n:
                return 1

            temp = 0
            for neigh in m[s]:
                temp = (temp + dfs(neigh, i + 1)) %  (10 ** 9 + 7)
            
            return temp


        ans = 0
        for i in range(10):    
            ans = (ans + dfs(i, 1)) %  (10 ** 9 + 7)

        return ans