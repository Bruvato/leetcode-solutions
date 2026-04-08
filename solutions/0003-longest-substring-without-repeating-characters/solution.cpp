class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // abcabccbb
        // L
        // R

        // pwwkew
        //

        // dvdf
        // abba
        //

        int res = 0;
        int l = 0;
        int n = s.length();

        vector<int> arr(128, -1);

        for (int r = 0; r < n; r++) {
            if (arr[s[r]] >= l) {
                l = arr[s[r]] + 1;
            }

            arr[s[r]] = r;
            res = max(res, r - l + 1);
        }

        return res;
    }
};
