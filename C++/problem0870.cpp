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
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
        vector<int> originalB = B;
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        vector<int>::iterator it;
        int k = 0;
        vector<int> tmp;
        map<int, vector<int>> d;
        for (it = A.begin(); it < A.end(); ++it)
        {
            if (*it > B[k])
            {
                d[B[k]].push_back(*it);
                k++;
            }
            else
            {
                tmp.push_back(*it);
                // cout << *it << endl;
            }
        }
        vector<int> ans;
        for (it = originalB.begin(); it < originalB.end(); ++it)
        {
            if (!d[*it].empty())
            {
                // cout << d[*it][d[*it].size()-1] << endl;
                ans.push_back(d[*it][d[*it].size()-1]);
                d[*it].pop_back();
            }
            else
            {
                // cout << tmp[tmp.size()] << endl;
                ans.push_back(tmp[tmp.size()-1]);
                tmp.pop_back();
            }
        }
        return ans;
    }
};

int main()
{
    // vector<int> A {2,7,11,15}, B {1,10,4,11}, ans;
    vector<int> A {12,24,8,32}, B {13,25,32,11}, ans;
    Solution solu;
    ans = solu.advantageCount(A, B);
    for (int k = 0; k < ans.size(); ++k)
    {
        cout << ans[k] << '\t';
    }
    cout << endl;
    return 0;
}