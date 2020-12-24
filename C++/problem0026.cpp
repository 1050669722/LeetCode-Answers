class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty())
        {
            return 0;
        }
        vector<int>::iterator i = nums.begin();
        vector<int>::iterator j;
        for (j = nums.begin(); j < nums.end(); ++j)
        {
            if (*j != *i)
            {
                i += 1;
                *i = *j;
            }
        }
        return i - nums.begin() + 1;
    }
};
