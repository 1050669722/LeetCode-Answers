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
//     vector<string> generatePossibleNextMoves(string s) {
//         vector<string> ans;
//         if (s.empty())
//         {
//             return ans;
//         }
//         string tmp = s;
//         for (int k = 0; k < tmp.size()-1; ++k)
//         {
//             if ( tmp[k]=='+' && tmp[k+1]=='+' )
//             {
//                 tmp[k] = '-';
//                 tmp[k+1] = '-';
//                 ans.push_back(tmp);
//                 tmp = s;
//             }
//         }
//         return ans;
//     }
// };

class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> ans;
        if (s.empty())
        {
            return ans;
        }
        string tmp = s;
        string::iterator it;
        for (it = tmp.begin(); it < tmp.end()-1; ++it)
        {
            if ( *it=='+' && *(it+1)=='+' )
            {
                *it = '-';
                *(it+1) = '-';
                ans.push_back(tmp);
                tmp = s;
            }
        }
        return ans;
    }
};

int main()
{
    string s = "++++";
    // string s = "";
    Solution solu;
    vector<string> ans = solu.generatePossibleNextMoves(s);
    vector<string>::iterator it;
    for (it = ans.begin(); it < ans.end(); ++it)
    {
        cout << *it << '\t';
    }
    cout << endl;
    return 0;
}