class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();

        int res = 0;
        int l = 0;

        for (int r = 0; r < n; r++) {
            if (prices[r] < prices[l]) {
                l = r;
            }

            int profit = prices[r] - prices[l];
            res = max(res, profit);
        }

        return res;
    }
};
