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
    string removeVowels(string S) {
        set<char> s {'a', 'e', 'i', 'o', 'u'};
        string ans;
        for (int k = 0; k < S.size(); ++k)
        {
            if (!s.count(S[k]))
            {
                ans.push_back(S[k]);
            }
        }
        return ans;
    }
};

int main()
{
    string S = "leetcodeisacommunityforcoders";
    Solution solu;
    string ans = solu.removeVowels(S);
    cout << ans << endl;
    return 0;
}