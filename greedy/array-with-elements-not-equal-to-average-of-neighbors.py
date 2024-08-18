class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        n1 = nums[: len(nums)//2 ]
        n2 = nums[len(nums)//2: ]

        ans = []
        s1 = s2 = 0

        while s1 < len(n1) and s2 < len(n2):
            ans.append(n2[s2])
            ans.append(n1[s1])

            s1 += 1
            s2 += 1

        if s1 < len(n1):
            ans += n1[s1:]
        if s2 < len(n2):
            ans += n2[s2:]

        return ans


        