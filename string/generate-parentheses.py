class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(open_paren, total_pair_form):
            nonlocal n
            if total_pair_form == n:
                ans.append("".join(paren_li))
                return
            
            if open_paren < n:
                paren_li.append("(")
                generate(open_paren + 1, total_pair_form)
                paren_li.pop()
            
            if open_paren > total_pair_form:
                paren_li.append(")")
                generate(open_paren, total_pair_form + 1)
                paren_li.pop()

        paren_li = []
        ans = []
        generate(0, 0)
        
        return ans

