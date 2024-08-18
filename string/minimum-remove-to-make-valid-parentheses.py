class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        st = []
        opening = 0
        
        for i,v in enumerate(s):
            st.append(v)
            
            if v=='(':
                opening+=1
            elif v==')':
                if opening:
                    opening-=1
                else:
                    st.pop()
                    
        ind = len(st) - 1
        while ind>=0 and opening>0:
            if st[ind] == '(':
                st[ind] = ''
                opening -=1
            ind-=1
            
        return ''.join(st)