class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0

        for word in words:
            if Counter(word) <= chars_count:
                ans += len(word)

        return ans