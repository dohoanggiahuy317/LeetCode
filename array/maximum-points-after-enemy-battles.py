class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        marked, curr = len(enemyEnergies) - 1, 0

        ans = 0

        while curr <= marked:
            if currentEnergy >= enemyEnergies[curr]:
                t = currentEnergy // enemyEnergies[curr]
                currentEnergy -= enemyEnergies[curr] * t
                ans += t
            else:
                if ans >= 1:
                    currentEnergy += enemyEnergies[marked]
                marked -= 1

            # print(curr, marked, currentEnergy, ans)
        return ans
