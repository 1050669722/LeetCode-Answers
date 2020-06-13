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
    int smallestRangeI(vector<int>& A, int K) {
        int MAX = A[0], MIN = A[0];
        for (int k = 0; k < A.size(); ++k)
        {
            if (A[k] > MAX)
            {
                MAX = A[k];
            }
            if (A[k] < MIN)
            {
                MIN = A[k];
            }
        }
        // cout << MAX << '\t' << MIN << endl;
        return max(MAX - MIN - 2*K, 0);
    }
};

int main()
{
    // vector<int> A {1, 3, 6};
    // int K = 3;
    vector<int> A {0, 10};
    int K = 2;
    Solution solu;
    int ans  =solu.smallestRangeI(A, K);
    cout << ans << endl;
    return 0;
}