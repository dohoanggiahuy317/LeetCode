class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        ans = 0
        for i in range(len(arr) - k):
            if s >= threshold * k:
                ans += 1
            s += arr[i+k] - arr[i]
              
        return ans + 1 if s >= threshold * k else ans