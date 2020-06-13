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
    int minIncrementForUnique(vector<int>& A)
    {
        if (A.empty())
        {
            return 0;
        }

        int sum = accumulate(A.begin(), A.end(), 0);
        sort(A.begin(), A.end(), less<int>());
        vector<int>::iterator it;
        for (it = A.begin()+1; it != A.end(); ++it)
        {
            if (*it <= *(it-1))
            {
                *it = *(it-1) + 1;
            }
        }
        return accumulate(A.begin(), A.end(), 0) - sum;
    }
};

int main()
{
    vector<int> A {3,2,1,2,1,7};
    Solution solu;
    int ans = solu.minIncrementForUnique(A);
    cout << ans << endl;
    return 0;
}