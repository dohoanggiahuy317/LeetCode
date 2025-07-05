class Solution:
    def findLucky(self, arr: List[int]) -> int:
        t = [(x, y) for x, y in Counter(arr).items()]
        t = sorted(t, reverse= True, key=lambda x: x[0])
        for x, y in t:
            if x == y:
                return x
        
        return -1