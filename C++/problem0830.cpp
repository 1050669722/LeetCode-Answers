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
    vector<vector<int>> largeGroupPositions(string S) {
        char letter = S[0];
        int start = 0, count = 1;
        map<vector<int>, vector<int>> d;
        // string::iterator it;
        // for (it = S.begin()+1; it != S.end(); ++it)
        // {
        //     if (*it == letter)
        //     {
        //         count++;
        //     }
        //     else
        //     {
        //         letter = *it;
        //     }
        // }
        for (int k = 1; k < S.size(); ++k)
        {
            if (S[k] == letter)
            {
                count++;
            }
            else
            {
                letter = S[k];
                start = k;
                count = 1;
            }
            if (count >= 3)
            {
                vector<int> tmpa {start, (int)letter}, tmpb {start, k};
                d[tmpa] = tmpb;
            }
        }
        vector<vector<int>> ans;
        for (map<vector<int>, vector<int>>::iterator it = d.begin(); it != d.end(); ++it)
        {
            ans.push_back(it->second);
        }
        return ans;
    }
};

int main()
{
    // string S = "abbxxxxzzy";
    string S = "aaa";
    // string S = "nnnhaaannnm";
    Solution solu;
    vector<vector<int>> ans = solu.largeGroupPositions(S);
    for (int p = 0; p < ans.size(); ++p)
    {
        for (int q = 0; q < ans[p].size(); ++q)
        {
            cout << ans[p][q] << '\t';
        }
        cout << endl;
    }
    return 0;
}