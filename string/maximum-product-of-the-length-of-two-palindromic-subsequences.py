class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        maxMask = 1 << n
        maxLen = [0] * maxMask
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        # Calculate the longest palindromic subsequence length for all possible subsequences
        for mask in range(1, maxMask):
            sub = ''.join(s[i] for i in range(n) if mask & (1 << i))
            if is_palindrome(sub):
                maxLen[mask] = len(sub)
        
        result = 0
        # Iterate over all possible pairs of disjoint subsequences
        for mask1 in range(1, maxMask):
            if maxLen[mask1] == 0:
                continue
            for mask2 in range(mask1 + 1, maxMask):
                if (mask1 & mask2) == 0 and maxLen[mask2] > 0:  # Ensure masks are disjoint
                    result = max(result, maxLen[mask1] * maxLen[mask2])
        
        return result