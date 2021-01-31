class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        map<int, int> m;
        for (int i = 0; i < nums.size(); ++i)
        {
            m.insert(pair<int, int>(i + 1, 0));
        }

        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            m[*it]++;
        }

        vector<int> ans;
        for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it)
        {
            if (it->second == 2)
            {
                ans.push_back(it->first);
            }
        }

        for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it)
        {
            if (it->second == 0)
            {
                ans.push_back(it->first);
            }
        }

        return ans;

    }
};
