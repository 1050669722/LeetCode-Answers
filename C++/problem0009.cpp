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

// class Solution {
// public:
//     bool isPalindrome(int x) {
//         if (x<0 || (x != 0 && x%10 == 0))
//         {
//             return false;
//         }
//         vector<int> tmp;
//         int x_tmp = x;
//         while (x)
//         {
//             tmp.push_back(x%10);
//             x /= 10;
//         }
//         int ans = 0, count = 0;
//         for (int k = tmp.size()-1; k > -1; --k)
//         {
//             ans += tmp[k] * pow(10, count);
//             count++;
//         }
//         // cout << ans;
//         return ans == x_tmp;
//     }
// };

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0 || (x != 0 && x%10 == 0))
        {
            return false;
        }
        int R = 0;
        while (x > R)
        {
            R = R*10 + x%10;
            x /= 10;
        }
        cout << x << '\t' << R << endl;
        return x == R || x == R / 10;
    }
};

int main()
{
    // int x = 121;
    // int x = 123;
    int x = 1221;
    Solution solu;
    bool ans = solu.isPalindrome(x);
    cout << boolalpha << ans << endl;
    return 0;
}