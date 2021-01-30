class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
        int min_ = -1;
        // for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        for (int i = 0; i < nums.size(); ++i)
        {
            if (nums[i] == i)
            {
                if (min_ == -1 or i < min_) #居然写了个or？ ||
                {
                    min_ = i;
                }
            }
        }
        return min_;
    }
};
