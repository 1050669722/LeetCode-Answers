class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int>::iterator i = nums.begin();
        for (vector<int>::iterator j = nums.begin(); j < nums.end(); ++j)
        {
            if (*j != val)
            {
                *i = *j;
                i += 1;
            }
        }
        return i - nums.begin();
    }
};
