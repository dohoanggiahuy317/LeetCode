class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def remove_invalid_parent(word, paren1, paren2):
            ans = []
            paren1_count = 0

            for char in word:
                if char == paren2:
                    if paren1_count == 0:
                        continue
                    else:
                        paren1_count -= 1
                        ans.append(char)

                else:
                    if char == paren1:
                        paren1_count += 1
                    ans.append(char)

            return ans[::-1]

        left2right = remove_invalid_parent(list(s), "(", ")")
        right2left = remove_invalid_parent(left2right, ")", "(")

        return "" .join(right2left)