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
    int hammingDistance(int x, int y) {
        int ans = 0;
        vector<int> X, Y;
        while (x)
        {
            X.push_back(x%2);
            x /= 2;
        }
        while (y)
        {
            Y.push_back(y%2);
            y /= 2;
        }

        int tmp = X.size() - Y.size();
        int lendiff = abs(tmp);
        // cout << lendiff << endl;
        // int lendiff = X.size() - Y.size();
        // if (lendiff>0)
        if (X.size() > Y.size())
        {
            for (int k = 0; k < lendiff; ++k)
            {
                Y.push_back(0);
            }
        }
        // else if (lendiff<0)
        else if (X.size() < Y.size())
        {
            // for (int k = 0; k < -lendiff; ++k)
            for (int k = 0; k < lendiff; ++k)
            {
                X.push_back(0);
            }
        }

        for (int k = 0; k < X.size(); ++k)
        {
            if (X[k] != Y[k])
            {
                ans += 1;
            }
        }
    return ans;
    }
};

int main()
{
    int x = 1;
    int y = 4;
    Solution solu;
    int ans = solu.hammingDistance(x, y);
    cout << ans << endl;
    // cout << abs(1-2) << endl;
    return 0;
}