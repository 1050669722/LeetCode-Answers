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
    int countSegments(string s) {
        if (s == "")
        {
            return 0;
        }
        int count = 0;
        string::iterator it;
        for (it = s.begin(); it < s.end(); ++it)
        {
            if (*it == ' ')
            {
                count++;
            }
        }
        return count+1;
    }
};

int main()
{
    string s = "Hello, my name is John";
    Solution solu;
    int ans = solu.countSegments(s);
    cout << ans << endl;
}