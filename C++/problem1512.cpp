class Solution {
public:
    int cal(int m)
    {
        return (int)(m * (m - 1) / 2);
    }

    int numIdenticalPairs(vector<int>& nums) {
        map<int, int> m;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            map<int, int>::iterator iter = m.find(*it);
            if (iter != m.end())
            {
                m[*it] += 1;
            }
            else
            {
                m.insert(pair<int, int>(*it, 1));
            }
        }
        
        int res = 0;
        for (map<int, int>::iterator iter = m.begin(); iter != m.end(); ++iter)
        {
            res += cal(iter->second);
        }

        return res;
    }
};
