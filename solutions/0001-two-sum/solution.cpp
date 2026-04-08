class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> hm;
        int n = nums.size();

        for (int i = 0; i < n; i++) {

            if (hm.contains(target - nums[i])) {
                return {i, hm[target - nums[i]]};
            }

            hm[nums[i]] = i;
        }

        return {0, 0};
    }
};
