class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def addParen(close_need, num_pair, curr_str):
            nonlocal ans
            if num_pair == n:
                if close_need > 0:
                    addParen(close_need - 1, num_pair, curr_str + ")")
                else:
                    ans.append(curr_str)
                    return
            else:
                if close_need > 0:
                    addParen(close_need - 1, num_pair, curr_str + ")")
                addParen(close_need + 1, num_pair + 1, curr_str + "(")

        ans = []
        addParen(0, 0, "")
        return ans