class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> nums_ori(nums);
        sort(nums.begin(), nums.end());
        map<int, int> res;
        vector<int> ans;

        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            if (res.find(*it) == res.end())
            {
                res.insert(pair<int, int>(*it, it - nums.begin()));
                // ans.push_back(it - nums.begin());
            }
            else
            {
                // ans.push_back(res[*it]);
            }
        }

        for (vector<int>::iterator it = nums_ori.begin(); it < nums_ori.end(); ++it)
        {
            ans.push_back(res[*it]);
        }

        return ans;
    }
};
