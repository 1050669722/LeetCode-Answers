class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> ans{first};
        for (vector<int>::iterator it = encoded.begin(); it < encoded.end(); ++it)
        {
            ans.push_back(*it ^ ans.back());
        }
        return ans;
    }
};
