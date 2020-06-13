#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

class Solution {
public:
    int fixedPoint(vector<int>& A) {
        int ans = -1; //既要定义类型，又要给初始值。
        for (int k = 0; k < A.size(); ++k)
        {
            // cout << k << '\t' << A[k] << endl;
            if (A[k] == k)
            {
                ans = k;
                break;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> A {-10,-5,0,3,7};
    Solution solu;
    int ans = solu.fixedPoint(A);
    cout << ans << endl;
    return 0;
}