class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # 1 1
        # 2 1
        # 3 1 3
        # 4 1 3 4
        # 5 1/ 3 4 5

        MOD = 10 ** 9 + 7
        queue = [(1, 1)]

        for day in range(1, n + 1):
            while queue and queue[0][0] + forget <= day:
                queue.pop(0)

            new_people = 0
            for know_day, people in queue:
                if know_day + delay <= day:
                    new_people += people
                else:
                    break
            if new_people > 0:
                queue.append((day, new_people))
        
        ans = 0
        for _, p in queue:
            ans = (ans + p) % MOD

        return ans

