class Solution {
public:
    bool isValid(string s) {
        if (s.length() % 2 == 1) {
            return false;
        }

        unordered_map<char, char> hm = {{'(', ')'}, {'{', '}'}, {'[', ']'}};

        stack<char> stk;

        for (int i = 0; i < s.length(); i++) {
            if (hm.contains(s[i])) {
                stk.push(s[i]);
            } else if (stk.empty() || hm[stk.top()] != s[i]) {
                return false;
            } else {
                stk.pop();
            }
        }

        return stk.empty();
    };
};
