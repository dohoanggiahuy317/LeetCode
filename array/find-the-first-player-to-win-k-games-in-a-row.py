from collections import deque


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if k >= n:
            return skills.index(max(skills))

        sk = skills[:]
        queue = deque(range(n))
        current_wins = 0
        while True:
            player1 = queue.popleft()
            player2 = queue.popleft()

            if skills[player1] > skills[player2]:
                queue.append(player2)
                queue.appendleft(player1)
                current_wins += 1
            else:
                queue.append(player1)
                queue.appendleft(player2)
                current_wins = 1

            if current_wins == k:
                return queue[0]
