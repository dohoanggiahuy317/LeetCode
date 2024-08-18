class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            m = min(strs)
            M = max(strs)

            ans = ""

            for i in range(len(m)):
                if i < len(M) and m[i] == M[i]:
                    ans += m[i]
                else:
                    break

            return ans