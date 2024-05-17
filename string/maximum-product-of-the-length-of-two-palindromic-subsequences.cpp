class Solution {
public:
    int maxProduct(string s) {
        int n = s.size();
        int maxMask = 1 << n;
        vector<int> maxLen(maxMask, 0);
        
        // Calculate the longest palindromic subsequence length for all possible subsequences
        for (int mask = 1; mask < maxMask; ++mask) {
            string sub;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    sub.push_back(s[i]);
                }
            }
            if (isPalindrome(sub)) {
                maxLen[mask] = sub.size();
            }
        }

        int result = 0;
        // Iterate over all possible pairs of disjoint subsequences
        for (int mask1 = 1; mask1 < maxMask; ++mask1) {
            if (maxLen[mask1] == 0) continue;
            for (int mask2 = mask1 + 1; mask2 < maxMask; ++mask2) {
                if ((mask1 & mask2) == 0 && maxLen[mask2] > 0) { // Ensure masks are disjoint
                    result = max(result, maxLen[mask1] * maxLen[mask2]);
                }
            }
        }
        
        return result;
    }

private:
    bool isPalindrome(const string& s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left++] != s[right--]) {
                return false;
            }
        }
        return true;
    }
};
