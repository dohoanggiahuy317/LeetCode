class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        VOWELS = "ueoai"
        
        vowel_count = sum([char in VOWELS for char in s[:k]])
        ans = vowel_count

        for right in range(k, len(s)):
            vowel_count -= s[right - k] in VOWELS
            vowel_count += s[right] in VOWELS

            ans = max(ans, vowel_count)

        return ans
                