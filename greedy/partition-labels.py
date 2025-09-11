class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_letter = {}
        for i, char in enumerate(s):
            last_letter[char] = i

        start = 0
        end = 0
        ans = []
        for i, char in enumerate(s):
            end = max(last_letter[char], end)

            if i != end:
                continue

            ans.append(end - start + 1)
            start = end + 1

        return ans
            