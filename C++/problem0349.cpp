class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> set2(nums2.begin(), nums2.end());
        // for (vector<int>::iterator it = nums2.begin(); it < nums2.end(); ++it)
        // {
        //     set2.insert(*it);
        // }

        set<int> s;
        for (vector<int>::iterator it = nums1.begin(); it < nums1.end(); ++it)
        {
            // if (set2.count(*it))
            if (set2.find(*it) != set2.end())
            {
                s.insert(*it);
            }
        }

        return vector<int> (s.begin(), s.end()); //匿名向量
    }
};
