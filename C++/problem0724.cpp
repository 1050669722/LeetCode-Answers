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
    int pivotIndex(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        int tmp = 0;
        for (int k = 0; k < nums.size(); ++k)
        {
            if (k > 0)
            {
                tmp += nums[k-1];
            }
            if (2*tmp == sum-nums[k])
            {
                return k;
            }
        }
        return -1;
    }
};

int main()
{
    vector<int> nums {1, 7, 3, 6, 5, 6};
    Solution solu;
    int ans = solu.pivotIndex(nums);
    cout << ans << endl;
    return 0;
}