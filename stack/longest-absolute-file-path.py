class Solution:
    def lengthLongestPath(self, input: str) -> int:
        whole = input.split("\n")
        temp = list(map(lambda x: len(x.split("\t")), whole))
        val = list(map(lambda x: x.split("\t")[-1], whole))
 
        ans = []
        hold = []
        res = 0

        for i in range(len(temp)):
            while ans and ans[-1] >= temp[i]:
                ans.pop(-1)
                hold.pop(-1)
            
            ans.append(temp[i])
            hold.append(val[i])

            if "." in val[i]:
                res = max(res, len("/".join(hold)))
                continue

        return res

        

        