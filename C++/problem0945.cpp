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
#include <numeric>

using namespace std;

class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        // return A.sum();
        // return accumulate(A, 6, 0);

        if (A.size() <= 0)
        {
            return 0;
        }

        int sum1 = 0;
        vector<int>::iterator it;
        for (it = A.begin(); it != A.end(); ++it)
        {
            sum1 += *it;
        }
        // cout << sum1 << endl;

        sort(A.begin(), A.end());

        for (it = A.begin()+1; it != A.end(); ++it)
        {
            if (*it <= *(it-1))
            {
                (*it) = *(it-1) + 1;
            }
        }
        
        // for (int k = 0; k < A.size(); ++k)
        // {
        //     cout << A[k] << '\t';
        // }
        // cout << endl;

        int sum2 = 0;
        for (it = A.begin(); it != A.end(); ++it)
        {
            sum2 += *it;
        }
        // cout << sum2 << endl;

        return sum2 - sum1;
    }
};

int main()
{
    // vector<int> A = {3,2,1,2,1,7};
    vector<int> A = {};
    Solution solu;
    int ans = solu.minIncrementForUnique(A);
    cout << ans << endl;
    return 0;
}