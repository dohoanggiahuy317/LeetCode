/**
 * @param {string} num
 * @return {string}
 */
var largestGoodInteger = function(num) {
    let ans = ""; // Initialize an empty string to store the result
    let empty = ""; // Initialize an empty string for a special case
    let temp = 0; // Initialize a variable to store the largest digit found
    let check = true; // Initialize a flag to check for a specific condition

    // Loop through the string to find the largest digit occurring thrice consecutively
    for (let i = 0; i < num.length - 2; i++) {
        // Check if the current digit is the same as the next two digits
        if (i + 2 < num.length && num[i] == num[i + 1] && num[i] == num[i + 2]) {
            // Convert the character digit to its integer equivalent and update 'temp'
            temp = Math.max(temp, parseInt(num[i]));
            check = false; // Update the flag to indicate the condition was met
        }
    }

    // If the condition was met (i.e., a triplet was found)
    if (check == false) {
        // Append the largest digit found three times to the 'ans' string
        for (let i = 0; i < 3; i++) {
            ans += temp.toString();
        }
    } else { // If no such triplet found
        return empty; // Return the empty string
    }

    return ans; // Return the result containing the largest good integer

};