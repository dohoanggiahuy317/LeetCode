class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        holder = set() # hold all the valid parenthesis

        def check_paren(temp, i, counter):
            nonlocal n
            if i == n: # removed k characters
                if counter == 0:
                    holder.add(temp)
                return

            if counter < 0: # number of ( is < 0
                return

            if s[i] == "(":
                check_paren(temp + s[i], i+1, counter + 1) # we take the current character
                check_paren(temp, i+1, counter)
                
            elif s[i] == ")":
                check_paren(temp + s[i], i+1, counter - 1) # we take the current character
                check_paren(temp, i+1, counter)
                
            else: # s[i] is an alphabet
                check_paren(temp + s[i], i+1, counter) # remove nothing, add alphabet character

        check_paren("", 0, 0)


        max_len = max( list( map(lambda x: len(x), list(holder) ) ) )
    
        ans = []
        for x in holder:
            if len(x) == max_len:
                    ans.append(x)
            
        return ans