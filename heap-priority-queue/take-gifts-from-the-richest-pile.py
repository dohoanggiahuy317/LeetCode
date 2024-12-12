import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = list(map(lambda x: -x, gifts))

        for i in range(k):
            curr_gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.sqrt(curr_gift)) )
        
        return -sum(gifts)
