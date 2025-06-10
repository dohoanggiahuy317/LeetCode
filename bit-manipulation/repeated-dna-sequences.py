class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        di = {
            "A": 1, "C": 2, "G": 3, "T": 4
        }

        curr_s = 0
        for i, val in enumerate(s[:10]):
            curr_s += 4 ** (9-i) * di[val]
        freq_set = {curr_s}
        ans = set()

        for right in range(10, len(s)):
            curr_s = (curr_s - di[s[right-10]] * (4 ** 9)) * 4 + di[s[right]]
            if curr_s in freq_set:
                ans.add(s[right-9:right+1]) 
            freq_set.add(curr_s)
        
        return list(ans)