class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> m;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            // map<int, int>::iterator iter = m.find(*it);
            // if (iter != m.end())
            if (m.find(*it) != m.end())
            {
                return true;
            }
            else
            {
                m.insert(pair<int, int>(*it, 1));
            }
        }
    return false;
    }
};
