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

using namespace std;

class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> tmp = heights;
        sort(heights.begin(), heights.end());

        // for (int k = 0; k < tmp.size(); ++k)
        // {
        //     cout << tmp[k] << '\t';
        //     cout << heights[k] << '\t';
        //     cout << endl;
        // }

        int ans = 0;
        for (int k = 0; k < heights.size(); ++k)
        {
            if (tmp[k] != heights[k])
            {
                ans += 1;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> heights {1,1,4,2,1,3};
    int ans = Solution().heightChecker(heights);
    cout << ans << endl;
    return 0;
}