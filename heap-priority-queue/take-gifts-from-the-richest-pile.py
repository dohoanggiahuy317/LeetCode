import math
import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        gifts = list(map(lambda x: -x, gifts))
        heapify(gifts)

        for i in range(k):
            curr_gift = -heappop(gifts)
            
            heappush(gifts, -int(math.sqrt(curr_gift)) )
        
        return -sum(gifts)
