class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        
        prevA, prevB = 0, 0 
        prevA2, prevB2 = 0, 0 
        
        for i in range(n):
            currentA = max(prevA + energyDrinkA[i], prevB2 + energyDrinkA[i])
            currentB = max(prevB + energyDrinkB[i], prevA2 + energyDrinkB[i])
            
            prevA2, prevB2 = prevA, prevB
            prevA, prevB = currentA, currentB
        
        return max(prevA, prevB)