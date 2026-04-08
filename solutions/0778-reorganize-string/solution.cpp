class Solution {
public:
    string reorganizeString(string s) {
        string res;
        unordered_map<char, int> hm;
        priority_queue<pair<int, char>> pq;
        char prev = '#';


        for (char c : s) {
            hm[c] ++;
        }

        for (auto [key, val] : hm) {
            pq.push({val, key});
        }

        while (!pq.empty()) {
            auto [freq, c] = pq.top();
            pq.pop();

            if (c == prev) {
                if (pq.empty()) return "";
                auto [freq2, c2] = pq.top();
                pq.pop();
                res += c2;
                if (freq2 - 1 > 0) pq.push({freq2 - 1, c2});
                pq.push({freq, c});
                prev = c2;

            } else {
                res += c;
                if (freq - 1 > 0) pq.push({freq - 1, c});
                prev = c;
            }



        }



        return res;
    }
};
