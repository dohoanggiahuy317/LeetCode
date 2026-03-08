class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()

