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
    int maximumSwap(int num) {
        vector<int> num1, num2;
        int temp = num;
        while (temp)
        {
            num1.push_back(temp%10);
            temp /= 10;
        }
        num2 = num1;
        reverse(num1.begin(), num1.end());
        // sort(num2.begin(), num2.end());
        // sort(num2.begin(), num2.end(), less<int>());
        // reverse(num2.begin(), num2.end());
        sort(num2.begin(), num2.end(), greater<int>());
        
        if (num1 == num2)
        {
            return num;
        }

        int k;
        for (k = 0; k < num1.size(); ++k)
        {
            if (num1[k] != num2[k])
            {
                break;
            }
        }
        // cout << k << endl;
        // cout << num2[k] << endl;

        int p;
        for (p = num1.size()-1; k > -1; --p)
        {
            // cout << num1[p] << num2[k] << endl;
            if (num1[p] == num2[k])
            {
                break;
            }
        }
        // cout << p << endl;
        // cout << num1[k] << '\t' << num1[p] << endl;
        // int tmp = num1[k];
        // num1[k] = num1[p];
        // num1[p] = tmp;
        num1[k] = num1[k] + num1[p];
        num1[p] = num1[k] - num1[p];
        num1[k] = num1[k] - num1[p];

        // vector<int>::iterator it;
        // for (it = num1.begin(); it != num1.end(); ++it)
        // {
        //     cout << *it << '\t';
        // }
        // cout << endl;

        int ans = 0;
        for (int k = 0; k < num1.size(); ++k)
        {
            // cout << num1[k] << '\t';
            ans *= 10;
            ans += num1[k];
        }
        return ans;

    }
};

int main()
{
    int num = 2736;
    // int num = 9973;
    Solution solu;
    int ans = solu.maximumSwap(num);
    cout << ans << endl;
    return 0;
}