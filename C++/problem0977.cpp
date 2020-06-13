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
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> ans;
        for (int k = 0; k < A.size(); ++k)
        {
            // ans.push_back(pow(A[k], 2));
            // ans.push_back((double)pow(A[k], (double)2));
            ans.push_back(A[k]*A[k]);
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};

int main()
{
    vector<int> A {-4,-1,0,3,10};
    Solution solu;
    vector<int> ans = solu.sortedSquares(A);
    vector<int>::iterator it;
    for (it = ans.begin(); it != ans.end(); ++it)
    {
        cout << *it << '\t';
    }
    cout << endl;
    return 0;
}