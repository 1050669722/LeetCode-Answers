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

// class Solution {
// public:
//     bool isMajorityElement(vector<int>& nums, int target) {
//         map<int, int> d;
//         for (int k = 0; k < nums.size(); ++k)
//         {
//             d[nums[k]] += 1;
//         }
//         return d[target] > nums.size()/2;
//     }
// };

// class Solution {
// public:
//     bool isMajorityElement(vector<int>& nums, int target) {
//         int ans = 0;
//         vector<int>::iterator it;
//         for (it = nums.begin(); it != nums.end(); ++it)
//         {
//             if (*it == target)
//             {
//                 ans++;
//             }
//         }
//         return ans > nums.size()/2;
//     }
// };

class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        if (nums.empty())
        {
            return false;
        }
        if (nums.size() == 1)
        {
            return nums[0] == target;
        }
        int p = 0, q = nums.size()-1;
        while (p < q)
        {
            if (nums[p] > target)
            {
                return false;
            }
            else
            {
                if (nums[p] < target)
                {
                    p++;
                }
            }
            if (nums[q] < target)
            {
                return false;
            }
            else
            {
                if (nums[q] > target)
                {
                    q--;
                }
            }
            if (nums[p] == target && nums[q] == target)
            {
                return q - p + 1 > nums.size()/2;
            }
        }
        return 0;
    }
};

int main()
{
    vector<int> nums {2,4,5,5,5,5,5,6,6};
    int target = 5;
    Solution solu;
    bool ans = solu.isMajorityElement(nums, target);
    cout << boolalpha << ans << endl;
    return 0;
}