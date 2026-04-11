class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        BIT_MAP = {"A": 0, "C": 1, "G": 2, "T": 3}
        
        if len(s) < 10:
            return []
        
        curr_window = 0
        for i in range(10):
            curr_window = curr_window * 4 + BIT_MAP[s[i]]
            
        seen = set()
        ans = set()
        seen.add(curr_window)
        
        for r in range(10, len(s)):
            curr_window = (curr_window - BIT_MAP[s[r - 10]] * (4 ** 9)) * 4 + BIT_MAP[s[r]]
            
            if curr_window in seen:
                ans.add(s[r - 9: r + 1])
            
            seen.add(curr_window)
        
        return list(ans)