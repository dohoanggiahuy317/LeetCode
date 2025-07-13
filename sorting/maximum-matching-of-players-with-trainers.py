class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        ans = 0
        p, t = 0, 0

        while p < len(players):
            while t < len(trainers) and players[p] > trainers[t]:
                t += 1
            if t < len(trainers):
                ans += 1
                t += 1
            p += 1
            
        
        return ans
