class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> dist;

        for (int i = 0; i < nums.size(); i++) {
            dist.push_back(i + nums[i]);
        }
        
        int curr_max = dist[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (curr_max < i) {
                return false;
            }
            if (curr_max < dist[i]) {
                curr_max = dist[i];
            }
        }

        return true;
    }
};
