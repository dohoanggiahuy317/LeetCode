class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int max_val = *max_element(nums.begin(), nums.end());
        int counter = 0;
        long l = 0;
        long ans = 0;

        for (int r = 0; r < nums.size(); ++r) {
            if (nums[r] == max_val) {
                counter += 1;
            }
            

            while (counter >= k) {
                if (nums[l] == max_val) {
                    counter -= 1;
                }
                
                l += 1;
            }

            ans += l;
        }

        return ans;
    }
};