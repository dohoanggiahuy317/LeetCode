class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        t1 = list(filter(lambda x: x >= 0, nums))
        t2 = list(filter(lambda x: x < 0, nums))

        ans = []
        for x in range(len(t1)):
            ans.append(t1[x])
            ans.append(t2[x])

        return ans