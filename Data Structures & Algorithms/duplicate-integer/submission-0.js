class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const set1 = new Set(nums);
        console.log(nums.length, set1.size)
        return nums.length > set1.size ? true : false;
    }
}
