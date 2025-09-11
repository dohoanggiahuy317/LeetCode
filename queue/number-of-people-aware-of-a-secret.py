class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # 1 1
        # 2 1
        # 3 1 3
        # 4 1 3 4
        # 5 1/ 3 4 5

        MOD = 10 ** 9 + 7
        queue = [1]

        for day in range(1, n + 1):
            while queue and queue[0] + forget <= day:
                queue.pop(0)

            for person in queue:
                if person + delay <= day:
                    queue.append(day)

        return len(queue) % MOD

