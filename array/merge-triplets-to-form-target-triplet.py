class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        init_trip = [1, 1, 1]

        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                init_trip = [ max(i[0], init_trip[0]), max(i[1], init_trip[1]), max(i[2], init_trip[2])]

        
        return init_trip == target