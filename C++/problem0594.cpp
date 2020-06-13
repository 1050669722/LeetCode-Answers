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

class Solution
{
    public:
        int findLHS(vector<int>& nums) {
        map<int, int> d;
        vector<int>::iterator it;
        for (it = nums.begin(); it < nums.end(); ++it)
        {
            // if (d.count(*it))
            // {
            //     d[*it]++;
            // }
            // else
            // {
            //     d[*it] = 1;
            // }
            d[*it]++;
        }
        map<int, int>::iterator iter;
        int ans = 0;
        for (iter = d.begin(); iter != d.end(); ++iter)
        {
            cout << iter->first << ' ' << iter->second << endl;
            if (d.count(iter->first-1))
            {
                ans = max(ans, iter->second+d[iter->first-1]);
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> nums {1,3,2,2,5,2,3,7};
    Solution solu;
    int ans = solu.findLHS(nums);
    cout << ans << endl;
    return 0;
}