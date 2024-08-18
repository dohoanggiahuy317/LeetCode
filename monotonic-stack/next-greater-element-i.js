/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function(nums1, nums2) {

    let ans = [];
    for (let i  = 0; i < nums1.length; i++ ) {
        let curr_val = nums1[i];

        let ind = nums2.indexOf(curr_val);

        let f = -1;

        for (let j = ind; j < nums2.length; j++ ) {
            if (nums2[j] > curr_val) {
                f = nums2[j];
                break;
            }
        }
        
        ans.push(f);
    }

    return ans;
    
};