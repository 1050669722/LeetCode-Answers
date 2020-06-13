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
    int numJewelsInStones(string J, string S) {
        set<char> s {};
        // set<char> s = {};
        // set<char> s;
        for (int k = 0; k < J.size(); ++k)
        {
            s.insert(J[k]);
        }
        int ans = 0;
        for (int k = 0; k < S.size(); ++k)
        {
            if (s.count(S[k]))
            {
                ans += 1;
            }
        }
        return ans;
    }
};

int main()
{
    string J = "aA";
    string S = "aAAbbbb";
    Solution solu;
    int ans = solu.numJewelsInStones(J, S);
    cout << ans << endl;
    return 0;
}