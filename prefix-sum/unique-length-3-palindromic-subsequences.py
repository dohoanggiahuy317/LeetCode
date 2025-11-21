class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        num_of_distinct_char = [0] * len(s)
        char_endpoint = {}

        for i, char in enumerate(s):
            if char not in char_endpoint:
                char_endpoint[char] = [i, -inf]
                num_of_distinct_char[i] = 1 if i == 0 else num_of_distinct_char[i - 1] + 1
            else:
                char_endpoint[char][1] = max(char_endpoint[char][1], i)
                num_of_distinct_char[i] = num_of_distinct_char[i - 1]

        ans = 0
        for (start, end) in char_endpoint.values():
            if end != -inf:
                ans += num_of_distinct_char[end] - (num_of_distinct_char[start - 1] if start > 0 else 0)

        return ans