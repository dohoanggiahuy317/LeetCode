class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def addParen(close_need, num_pair, curr_str):
            nonlocal ans
            if num_pair == n and close_need == 0:
                ans.append(curr_str)
                return
            
            if not num_pair == n:
                addParen(close_need + 1, num_pair + 1, curr_str + "(")
            if close_need > 0:
                addParen(close_need - 1, num_pair, curr_str + ")")

        ans = []
        addParen(0, 0, "")
        return ans