class Solution {
public:
    bool hasTrailingZeros(vector<int>& nums) {
    int n = nums.size();

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            // Check if the bitwise OR has a trailing zero
            if ((nums[i] | nums[j]) % 2 == 0) {
                return true;
            }
        }
    }

    return false;
    }
};