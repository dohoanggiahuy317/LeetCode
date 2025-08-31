class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def addParen(close_need, num_pair):
            nonlocal ans, candidate
            if num_pair == n and close_need == 0:
                ans.append("".join(candidate))
                return
            
            if not num_pair == n:
                candidate.append("(")
                addParen(close_need + 1, num_pair + 1)
                candidate.pop()
            if close_need > 0:
                candidate.append(")")
                addParen(close_need - 1, num_pair)

        ans = []
        candidate = []
        addParen(0, 0)
        return ans