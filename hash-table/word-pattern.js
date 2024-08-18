/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    let d1 = {};
    let d2 = {}

    let sl = s.split(" ")
    let pl = pattern.split("")

    if (sl.length !== pl.length) {
        return false;
    }

    for (let i = 0; i < sl.length; i++) {
        if (sl[i] === "constructor") {
            sl[i] = "contructor_haha"
        }
        if (pl[i] in d1 === false && sl[i] in d2 === false) {
            d1[pl[i]] = sl[i];
            d2[sl[i]] = pl[i];
        } else {
            if (d1[pl[i]] === sl[i] && d2[sl[i]] === pl[i]) {
                continue;
            }
            return false;
        }
    }

    // console.log(sl, pl, d1, d2);
    return true;
};