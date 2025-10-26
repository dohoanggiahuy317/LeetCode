class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # 1 1 1 1
        # _ 2 2 2 2
        
        # 1 _ 1 1 1
        # _ 2 _ 2 2 2


        # work on things with larger grow time first so that we will have time to plant others
        # 1 2
        # 2 1
        # 3 2
        # 2 1

        
        # 0: 0 2
        # 1: 0 2
        # 2: 1 1
        # 3: 2 1

        # 1 1 1 1 1 X
        # - - 0 0 0 X
        # - - - 2 - 2 2 X
        # - - - - 3 - 3 3 X


        pq = []

        for plant, grow in zip(plantTime, growTime):
            heapq.heappush(pq, (-plant, -grow))

        day = 0
        ans = 0
        while pq:
            p, g = heapq.heappop(pq)
            p = -p
            g = -g
            
            day += 1
            p -= 1
            
            if p > 0:
                heapq.heappush(pq, (-p, -g))
            else:
                ans = max(ans, day + g)

            # print(pq, ans, day)

        return ans