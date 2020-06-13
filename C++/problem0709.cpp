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
    string toLowerCase(string str) {
        for (int k = 0; k < str.size(); ++k)
        {
            // if ('A'<=str[k] && str[k]<='Z')
            if (65<=str[k] && str[k]<=90)
            {
                str[k] += 32;
            }
        }
        return str;
    }
};

int main()
{
    string str = "Hello";
    Solution solu;
    string ans = solu.toLowerCase(str);
    cout << ans << endl;
    return 0;
}