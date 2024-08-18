/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {

    if (nums.length == 1) {
        return 0;
    } 

    let left = 0;
    let right = 0;
    let ans = -1;

    for (let i = 1; i < nums.length; i++) {
        right += nums[i];
    }

    for (let j = 0; j < nums.length; j++) {
        console.log(left, right);
        if (left == right) {
            ans = j;
            break
        }

        left += nums[j];

        if (j < nums.length - 1) {
            right -= nums[j+1];
        }
        
    }
    
    return ans;
};