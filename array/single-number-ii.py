class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict = [[], []]
        
        for i in nums:
            if i in mydict[0]:
                mydict[0].remove(i)
                mydict[1].append(i)
            if i not in mydict[0] and i not in mydict[1]:
                mydict[0].append(i)
        
        return mydict[0][0]