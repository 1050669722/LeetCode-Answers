// class Solution {
// public:
//     vector<int> decompressRLElist(vector<int>& nums) {
//         map<int, int> m;
//         for (vector<int>::iterator it = nums.begin(); it < nums.end(); it += 2)
//         {
//             m.insert(pair<int, int>(*it, *(it + 1)));
//         }

//         vector<int> ans;
//         for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it)
//         {
//             for (int i = 0; i < it->first; ++i)
//             {
//                 ans.push_back(it->second);
//             }
//         }

//         return ans;
//     }
// };


class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> freqs, vals, ans;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); it += 2)
        {
            freqs.push_back(*it);
            vals.push_back(*(it + 1));
        }

        for (int i = 0; i < freqs.size(); ++i)
        {
            for (int j = 0; j < freqs[i]; ++j)
            {
                ans.push_back(vals[i]);
            }
        }

        return ans;
    }
};
