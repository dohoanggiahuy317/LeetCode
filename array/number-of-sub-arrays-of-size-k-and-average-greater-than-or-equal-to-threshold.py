class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        curr_sum = sum(arr[:k])

        if curr_sum/k >= threshold:
            count += 1

        for i in range(len(arr) - k):
            curr_sum = curr_sum - arr[i] + arr[i + k]
            
            if curr_sum/k >= threshold:
                count += 1

        
        return count