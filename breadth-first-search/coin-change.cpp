class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0){
            return 0;
        }

        int memoir[amount+1];

        for (int i = 1; i < amount+1; i++) {
            memoir[i] = pow(2, 16);

            for (int x: coins) {
                if (i == x) {
                    memoir[i] = 1;
                    break;
                }

                if (i-x > 0 && memoir[i] > memoir[i-x] + 1) {
                    memoir[i] = memoir[i-x] + 1;
                }
            }
        }

        return memoir[amount] == pow(2, 16) ? -1 : memoir[amount];
    }
};