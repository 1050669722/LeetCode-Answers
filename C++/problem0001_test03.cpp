class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            map<int, int>::iterator it = m.find(target - nums[i]);
            if (it != m.end())
            // if (m.count(target - nums[i]) != 0)
            {
                // return {m[target - nums[i]], i};
                // return vector<int>{m[target - nums[i]], i};
                // return vector<int>{(*it).second, i};
                return vector<int>{it->second, i};
            }
            m.insert(pair<int, int>(nums[i], i));
            // m.insert(make_pair(nums[i], i));
            // m.insert(map<int, int>::value_type(nums[i], i));
            // m[nums[i]] = i;
        }
        return {};
        // return vector<int>{};
    }
};
