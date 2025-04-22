/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
    const output = {};
    let key = ""
    for (const ele of this) {
        key = fn(ele)
        if (key in output) {
            output[key].push(ele);
        } else {
            output[key] = [ele];
        }
    }

    return output;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */