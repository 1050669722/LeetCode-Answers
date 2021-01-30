class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int vote = 0, ans/* = nums[0]*/;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            // cout << vote << endl;
            // cout << *it << ' ' << ans << endl;
            if (vote == 0)
            {
                ans = *it;
            }
            if (*it == ans)
            {
                vote++;
            }
            else
            {
                vote--;
            }
        }
        return ans;
    }
};
