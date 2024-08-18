class Solution {
public:
   // Function to find the maximum distance between elements of two different rows in a 2D vector
   int maxDistance(vector<vector<int>>& v) {
       // Initialize the maximum and minimum elements from the first row.
       int mx = v[0][v[0].size() - 1], mn = v[0][0];
       int n = v.size(), ans = 0;

       // Traverse from the second row to the last row to compute the maximum distance.
       for (int i = 1; i < n; i++) {
           // Update the maximum distance considering the current row's elements.
           ans = max({ans, v[i][v[i].size() - 1] - mn, mx - v[i][0]});
           // Update the minimum and maximum values encountered so far.
           mn = min(mn, v[i][0]);
           mx = max(mx, v[i][v[i].size() - 1]);
       }

       // Reinitialize the maximum and minimum values with the last row's elements.
       mx = v[n-1][v[n-1].size() - 1];
       mn = v[n-1][0];

       // Traverse from the second-to-last row back to the first row.
       for (int i = n - 2; i >= 0; i--) {
           // Again, update the maximum distance considering the current row's elements.
           ans = max({ans, v[i][v[i].size() - 1] - mn, mx - v[i][0]});
           // Update the minimum and maximum values encountered so far.
           mn = min(mn, v[i][0]);
           mx = max(mx, v[i][v[i].size() - 1]);
       }

       // Return the maximum distance found.
       return ans;
   }
};