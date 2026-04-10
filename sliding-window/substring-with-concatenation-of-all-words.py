class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        w = len(words[0])
        len_s, len_words = len(s), len(words) * w
        
        w_counter = Counter(words)
        ans = []

        for i in range(len_s):
            sub_s = s[i:i + len_words]
            sub_s_counter = Counter(sub_s[j: j + w] for j in range(0, len_words, w))

            if w_counter == sub_s_counter:
                ans.append(i)

        return ans
        