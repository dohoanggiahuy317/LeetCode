/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    let s1 = 0; let t1 = 0;

    while (t1 < t.length) {
        if (s.slice(s1, s1+1) === t.slice(t1, t1+1)) {
            s1 += 1;
        }
        t1 += 1;
    }

    if (s1 == s.length) {
        return true;
    }

    return false;
};