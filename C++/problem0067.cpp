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
    string addBinary(string a, string b) {
        vector<char> A, B;
        for (int k = a.size()-1; k > -1; --k)
        {
            A.push_back(a[k]);
        }
        // string::iterator it;
        // for (it = b.end()-1; it >= b.begin(); --it)
        // for (it = b.end()-1; it > b.begin()-1; --it)
        for (string::iterator it = b.end()-1; it > b.begin()-1; --it)
        {
            B.push_back(*it);
        }
        // for (int k = b.size()-1; k > -1; --k)
        // {
        //     B.push_back(b[k]);
        // }
        // for (int k = 0; k < B.size(); ++k)
        // {
        //     cout << B[k] << '\t';
        // }
        // cout << endl;
        int length = max(a.size(), b.size());
        int diff = length - min(a.size(), b.size());
        if (a.size() > b.size())
        {
            for (int k = 0; k < diff; ++k)
            {
                B.push_back('0');
            }
        }
        else
        {
            if (a.size() < b.size())
            {
                for (int k = 0; k < diff; ++k)
                {
                    A.push_back('0');
                }
            }
        }

        string ans;
        int carry = 0;
        for (int k = 0; k < length; ++k)
        {
            char tmp = (char)( ( ((int)a[k]) ^ ((int)b[k]) ) ^ carry );
            ans.push_back(tmp);
            carry = ( ((int)a[k]) & ((int)b[k]) ) | ( ((int)a[k]) & carry ) | ( carry & ((int)b[k]) );
        }
        if (carry == 1)
        {
            ans.push_back((char)carry);
        }
        cout << ans << endl;
        return ans;
    }
};

int main()
{
    string a = "11", b = "1";
    // string a = "1010", b = "1011";
    Solution solu;
    string ans = solu.addBinary(a, b);
    cout << ans << endl;
    cout << "Hello World!" << endl;
    return 0;
}