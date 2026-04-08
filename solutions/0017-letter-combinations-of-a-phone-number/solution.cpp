class Solution {
public:
    vector<string> res;
    unordered_map<char, string> hm = {
        {'2', "abc"}, {'3', "def"},  {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"},
    };
    string curr;
    string digits;

    vector<string> letterCombinations(string digits) {
        this->digits = digits;
        backtrack(0, curr);

        return res;
    }

    void backtrack(int i, string& curr) {
        if (i >= digits.length()) {
            res.push_back(curr);
            return;
        }

        string letters = hm[digits[i]];

        for (int j = 0; j < letters.length(); j++) {
            char c = letters[j];
            curr += c;
            backtrack(i + 1, curr);
            curr.pop_back();
        }
    }
};
