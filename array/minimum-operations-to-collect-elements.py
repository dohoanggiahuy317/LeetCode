class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target = set([i for i in range(1, k + 1)])
        ans = 0

        while len(target) > 0:
            last_elem = nums.pop()
            if last_elem in target:
                target.remove(last_elem)

            ans += 1
        
        return ans
