class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        pair_count = defaultdict(int)
        #pair_count[j] = number of i such as i < j and nums[j] - nums[i] = diff
        triplet = 0

        for k in range(n):
            for j in range(k):
                if nums[k] - nums[j] == diff:
                    pair_count[k] += 1
                    triplet += pair_count[j]

        return triplet
