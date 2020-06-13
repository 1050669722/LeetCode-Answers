#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

string STR(int i)
{
    string a;
    while (i)
    {
        int tmp = i%10;
        i /= 10;
        int diff = tmp - 0;
        a.push_back((char)(48 + diff));
    }
    reverse(a.begin(), a.end());
    return a;
};

class Solution {
public:
    string countAndSay(int n) {
        if (n == 1)
        {
            return STR(1);
        }
        string s = "1";
        vector<char> stack;
        stack.push_back(s[0]);
        for (int k = 1; k < n; ++k)
        {
            string tmp;
            for (int p = 1; p < s.size(); ++p)
            {
                if (!stack.empty() && stack[stack.size()-1] != s[p])
                {
                    tmp.push_back(STR(stack.size()*10 + stack[stack.size()-1]));
                }
                stack.push_back(s[p]);
            }
        }
    }
};

int main()
{
    int n = 5;
    Solution solu;
    string ans = solu.countAndSay(n);
    cout << ans << endl;
    // int a = 123;
    // string b = STR(a);
    // cout << typeid(b).name() << '\t' << b << endl;
    return 0;
}

