class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        
        freq = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = curr_sum if if len(freq) >= m else 0

        for i in range(k, len(nums)):
            freq[nums[i]] += 1
            freq[nums[i - k]] -= 1

            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]

            if len(freq) >= m:
                max_sum = max(max_sum, curr_sum)

        return max_sum