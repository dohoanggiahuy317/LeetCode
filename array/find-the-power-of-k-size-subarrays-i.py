class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        results = []
        
        for i in range(len(nums) - k + 1):
            subarray = nums[i:i + k]
            if subarray == list(range(min(subarray), min(subarray) + k)):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results