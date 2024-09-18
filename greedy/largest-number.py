class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        m = 0
        for x in nums:
            m = max(m, len(str(x)))
        
        nnums = list(map(lambda x: str(x) + str(x)[-1] * (m-len(str(x))), nums))

        nnums = sorted(zip(nnums, list(map(str, nums))), reverse = True, key=lambda x: x[0])

        nnums = list(map(lambda x: x[1], nnums))


        return "".join(nnums)