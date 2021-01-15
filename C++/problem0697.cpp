class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        map<int, vector<int>> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (m.find(nums[i]) == m.end())
            {
                m.insert(pair<int, vector<int>>(nums[i], vector<int>{i}));
            }
            else
            {
                m[nums[i]].push_back(i);
            }
        }
        
        vector<int> tmp{nums[0]}; 
        int max_ = 1;
        for (map<int, vector<int>>::iterator it = m.begin(); it != m.end(); ++it)
        {
            if (it->second.size() > max_)
            {
                tmp.clear();
                tmp.push_back(it->first);
                max_ = it->second.size();
            }
            else if (it->second.size() == max_)
            {
                tmp.push_back(it->first);
            }
        }
        
        int min_ = nums.size();
        for (vector<int>::iterator it = tmp.begin(); it < tmp.end(); ++it)
        {
            if (m[*it].back() - m[*it].front() + 1 < min_)
            {
                min_ = m[*it].back() - m[*it].front() + 1;
            }
        }
        return min_;

    }
};
