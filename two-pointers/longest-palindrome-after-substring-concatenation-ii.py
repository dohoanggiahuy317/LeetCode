class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:

        def findMaxPalindrome(temp, left, right):

            while left >= 0 and right < len(temp) and temp[left] == temp[right]:
                left -= 1
                right += 1

            return right - left - 1

        m, n = len(s), len(t)
        ans = 0

        for i in range(m+1):
            for j in range(n+1):
                temp = s[:i] + t[j:]
                for k in range(len(temp)):
                    t1 = findMaxPalindrome(temp, k, k+1)
                    t2 = findMaxPalindrome(temp, k, k)
                    ans = max([ans, t1, t2])

        return ans