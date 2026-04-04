class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k])
        count = int(curr_sum >= (threshold * k))

        for i in range(k, len(arr)):
            curr_sum += arr[i]
            curr_sum -= arr[i - k]
            count += int(curr_sum >= (threshold * k))

        return count