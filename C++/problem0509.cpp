#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <windows.h>

using namespace std;

class Solution {
public:
    int fib(int N) {
        if (N == 0)
            return 0;
        if (N == 1)
            return 1;
        vector<int> a {0, 1};
        for (int k = 2; k < N+1; ++k)
        {   
            // cout << a[k-2] << '\t' << a[k-1] << endl;
            a.push_back(a[k-1]+a[k-2]);
        }
        // cout << a.size() << endl;
        return a[a.size()-1];
    }
};

int main()
{
    int N = 30;
    Solution solu;
    // int ans = 0; 
    // ans = solu.fib(N);
    int ans = solu.fib(N);
    cout << ans <<endl;
}