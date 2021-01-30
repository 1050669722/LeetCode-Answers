class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        set<int> tmp;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            if (tmp.find(*it) == tmp.end())
            {
                tmp.insert(*it);
            }
            else
            {
                return *it;
            }
        }
        return 0;
    }
};
