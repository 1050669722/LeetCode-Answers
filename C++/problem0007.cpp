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
    int reverse(int x) {
        if (x <= INT32_MIN || x > INT32_MAX)
        {
            return 0;
        }
        int p = 1;
        if (x < 0)
        {
            p = -1;
            x *= -1;
        }
        vector<int> tmp;
        while (x)
        {
            tmp.push_back(x%10);
            x /= 10;
        }
        int ans = 0;
        int count = 0;
        for (int k = tmp.size()-1; k > -1; --k)
        {
            // cout << tmp[k] << endl;
            ans += tmp[k] * pow(10, count);
            count++;
        }
        if (ans <= INT32_MIN || ans > INT32_MAX)
        {
            return 0;
        }
        ans *= p;
        return ans;
    }
};

int main()
{
    int x = 123;
    Solution solu;
    int ans = solu.reverse(x);
    cout << ans << endl;
    // cout << INT32_MIN << endl;
    // cout << INT32_MAX << endl;
    return 0;
}