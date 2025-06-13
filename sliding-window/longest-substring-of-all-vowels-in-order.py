class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        left = 0
        ans = 0
        count = 1
        for right in range(len(word)):
            if right == left:
                continue
            elif word[right] >= word[right - 1]:
                count += int(word[right] != word[right - 1])
                if count == 5:
                    ans = max(ans, right - left + 1)
            else:
                count = 1
                left = right
        return ans
            