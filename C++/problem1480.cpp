class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            sum += *it;
            *it = sum;
        }
        return nums;
    }
};
