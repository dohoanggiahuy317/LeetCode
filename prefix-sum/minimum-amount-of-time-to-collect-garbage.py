class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        p1 = 0
        p2 = 0
        p3 = 0

        prev1 = 0
        prev2 = 0
        prev3 = 0

        for i in range(1, len(garbage)):
            house = garbage[i]

            visited1 = False
            visited2 = False
            visited3 = False

            prev1 += travel[i-1]
            prev2 += travel[i-1]
            prev3 += travel[i-1]

            for t in house:
                if t == "M":
                    if visited1 is False:
                        p1 += prev1
                        prev1 = 0
                        visited1 = True
                    p1 += 1
                if t == "G":
                    if visited2 is False:
                        p2 += prev2
                        prev2 = 0                        
                        visited2 = True
                    p2 += 1
                if t == "P":
                    if visited3 is False:
                        p3 += prev3
                        prev3 = 0                        
                        visited3 = True
                    p3 += 1

        for t in garbage[0]:
            if t == "M":
                p1 += 1
            if t == "G":
                p2 += 1
            if t == "P":
                p3 += 1

        return p1 + p2 + p3