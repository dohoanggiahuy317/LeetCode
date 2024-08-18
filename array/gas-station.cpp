class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> gain;
        int ans = 0;
        int curr_gain = 0;
        int total_gain = 0;
        int n = gas.size();

        for (int i = 0; i < n; i++) {
            int diff = gas[i] - cost[i];
            curr_gain += diff;
            total_gain += diff;

            if (curr_gain < 0) {
                curr_gain = 0;
                ans = i+1;
            }
        }

        if (total_gain < 0) {
            return -1;
        } else {
            return ans % n;
        }
    } 
};