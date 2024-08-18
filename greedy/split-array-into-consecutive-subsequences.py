class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        li = [ [nums[0]] ]

        for x in nums[1:]:
            li.sort(key = len)
            found = False
            for l in li:
                if x == l[-1] + 1:
                    l.append(x)
                    found = True
                    break
            if not found:
                li.append([x])


        for l in li:
            if len(l) < 3:
                return False
        return True
