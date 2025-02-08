class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        ans = 0

        for direction in [{"N", "E"}, {"N", "W"}, {"S", "E"}, {"S", "W"}]:
            k_left = k
            dist = 0

            for char in s:
                if char in direction or k_left > 0:
                    dist += 1    
                    k_left -= 1 if char not in direction else 0
                else:
                    dist -= 1

                ans = max(ans, dist)

        return ans
