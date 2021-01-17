class Solution {
public:
    string reverseLeftWords(string s, int n) {
        string ans = s.substr(n, s.size() - n);
        // ans += s.substr(0, n);
        ans.append(s.substr(0, n));
        return ans;
    }
};
