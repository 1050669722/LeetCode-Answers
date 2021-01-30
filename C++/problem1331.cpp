class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        map<int, int> tmp;
        vector<int> ans, arr_copy(arr);
        sort(arr.begin(), arr.end());
        int flag = 0;
        for (vector<int>::iterator it = arr.begin(); it < arr.end(); ++it)
        {
            if (tmp.find(*it) == tmp.end())
            {
                tmp.insert(pair<int, int>(*it, (it - arr.begin() + 1 - flag)));
                // tmp.insert(make_pair(*it, (it - arr.begin() + 1 - flag)));
                // tmp.insert(map<int, int>::value_type(*it, (it - arr.begin() + 1 - flag)));
                // tmp[*it] = it - arr.begin() + 1 - flag;
            }
            else
            {
                flag++;
            }
        }
        for (vector<int>::iterator it = arr_copy.begin(); it < arr_copy.end(); ++it)
        {
            ans.push_back(tmp[*it]);
        }
        return ans;
    }
};
