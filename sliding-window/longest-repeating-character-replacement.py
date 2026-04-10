class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        lefts = {chr(ord("A") + letter_ord): 0 for letter_ord in range(26)}
        swap_used = {chr(ord("A") + letter_ord): 0 for letter_ord in range(26)}
        ans = 0

        for r, char in enumerate(s):

            for letter_ord in range(26):
                letter = chr(ord("A") + letter_ord)

                if letter == char:
                    continue

                swap_used[letter] += 1
                
                while swap_used[letter] > k:
                    if s[lefts[letter]] != letter:
                        swap_used[letter] -= 1

                    lefts[letter] += 1

            ans = max(ans, r - min(lefts.values()) + 1)

        return ans
