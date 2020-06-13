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
    int sumOfDigits(vector<int>& A) {
        int Min = INT32_MAX;
        for (int k = 0; k < A.size(); ++k)
        {
            if (A[k] < Min)
            Min = A[k];
        }
        int ans = 0;
        while (Min)
        {
            ans += Min%10;
            Min /= 10;
        }
        if (ans%2)
            return 0;
        else
        {
            return 1;
        } 
    }
};

int main()
{
    vector<int> A {34,23,1,24,75,33,54,8};
    Solution solu;
    int ans = solu.sumOfDigits(A);
    cout << ans << endl;
    // cout << min(1,2) << endl;
    return 0;
}