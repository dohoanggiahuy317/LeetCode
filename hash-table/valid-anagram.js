/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let s1 = ""; let t1 = "";
    let sl = s.split("").sort();
    let tl = t.split("").sort();
    while (sl.length !== 0) {
        s1 += sl.pop();
    }
    while (tl.length !== 0) {
        t1 += tl.pop();
    }
    // console.log(s1, t1);
    return s1 == t1;
};