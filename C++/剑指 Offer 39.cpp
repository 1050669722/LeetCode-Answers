class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // sort(nums.begin(), nums.end());
        // return nums[(int)(nums.size() / 2)];

        int vote = 0, x = nums[0];
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            if (vote == 0)
            {
                x = *it;
            }
            if (*it == x)
            {
                vote++;
            }
            else
            {
                vote--;
            }
        }
        return x;
    }
};
