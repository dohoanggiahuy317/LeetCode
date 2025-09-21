class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group_freq = []
        
        curr_num = s[0]
        count = 0
        for char in s + " ":
            if curr_num == char:
                count += 1
            else:
                group_freq.append(count)
                count = 1
                curr_num = char

        ans = 0
        for prev, after in pairwise(group_freq):
            ans += min(prev, after)
        
        return ans