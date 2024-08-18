class Solution:
    def minOperations(self, k: int) -> int:
        ans = float('inf')
        for inc in range(0, k):
            new_num = 1 + inc
            if k % new_num == 0:
                left = int(k / new_num)
            else:
                left = int(k/new_num) + 1
                
            # print(inc, left)
            ans = int(min(ans, inc + left - 1))
            
        return ans