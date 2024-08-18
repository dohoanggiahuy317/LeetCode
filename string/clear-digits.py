class Solution:
    def clearDigits(self, s: str) -> str:
        st = []

        for char in s:
            if char.isdigit() and len(st) > 0:
                st.pop(-1)
            else:
                st.append(char)
                
        return "".join(st)
        