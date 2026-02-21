class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        positive = [x*x for x in nums if x >= 0]
        negative = [x*x for x in nums if x < 0]
        negative.sort()

        i = j = 0
        out = []

        while i < len(positive) and j < len(negative):
            if positive[i] <= negative[j]:
                out.append(positive[i])
                i += 1
            else:
                out.append(negative[j])
                j += 1
        
        out.extend(positive[i:])
        out.extend(negative[j:])
        
        return out