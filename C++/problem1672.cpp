#include <numeric>

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_ = 0;
        for (vector<vector<int>>::iterator it = accounts.begin(); it < accounts.end(); ++it)
        {
            int tmp = accumulate((*it).begin(), (*it).end(), 0);
            if (tmp > max_)
            {
                max_ = tmp;
            }
        }
        return max_;
    }
};
