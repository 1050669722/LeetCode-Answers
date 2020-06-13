#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <windows.h>
#include <string>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // map<int, int> d;
        // // vector<int>::iterator iter;
        // // for (iter = nums.begin(); iter != nums.end(); ++iter)
        // for (int k = 0; k < nums.size(); ++k)
        // {
        //     if (d.count(target-nums[k]) == 0)
        //     {
        //         d[nums[k]] = k;
        //     }
        //     else
        //     {
        //         vector<int> ans = {k, d[target-nums[k]]};
        //         return ans;
        //     }
        // vector<int> tmp = {0};
        // return tmp;
        // }
        map<int, int> d;
        vector<int> ans;
        for (int k = 0; k < nums.size(); ++k)
        {
            if (d.count(target-nums[k])==0)
            {
                d[nums[k]] = k;
            }
            else
            {
                ans.push_back(k);
                ans.push_back(d[target-nums[k]]);
                break;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> nums {2, 7, 11, 15};
    int target = 9;
    Solution solu;
    vector<int> ans = solu.twoSum(nums, target);
    for (int k = 0; k < ans.size(); ++k)
    {
        cout << ans[k] << '\t';
    }
    cout << endl;
    return 0;
}