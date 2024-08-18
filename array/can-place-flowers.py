class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if len(flowerbed) == 1:
            return flowerbed[0] == 0 or n < 1
        if len(flowerbed) == 2:
            return (flowerbed[0] + flowerbed[1] == 0 and n < 2) or n == 0

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i > 0 and i < len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1

        return count >= n
                    
        