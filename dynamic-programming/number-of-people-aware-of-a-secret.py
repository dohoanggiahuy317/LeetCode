class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        MOD = 10 ** 9 + 7
        queue = [(1, 1)]

        # Go through each day
        for day in range(1, n + 1):
            # People forget
            while queue and queue[0][0] + forget <= day:
                queue.pop(0)

            # new people heard story
            new_people = 0
            for know_day, people in queue:
                if know_day + delay <= day:
                    new_people += people
                else:
                    break
            if new_people > 0:
                queue.append((day, new_people))
        
        # answer
        ans = 0
        for _, p in queue:
            ans = (ans + p) % MOD

        return ans

