#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int res = nums[0];
        for (int k = 1; k < nums.size(); ++k)
        {
            if (ans < 0)
            {
                ans = 0;
            }
            ans += nums[k];
            // cout << ans <<endl;
            res = max(res, ans);
        }
        return res;
    }
};

int main()
{
    vector<int> nums {-2,1,-3,4,-1,2,1,-5,4};
    Solution solu;
    int ans = solu.maxSubArray(nums);
    cout << ans << endl;
    return 0;
}