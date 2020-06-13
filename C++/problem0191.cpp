#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <windows.h>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans = 0;
        while (n)
        {
            ans += n%2;
            // n = n/2;
            n /= 2;
            // n = (int)n/2;
            // n = int(n/2);
        }
        return ans;
    }
};

int main()
{
    uint32_t n = 00000000000000000000000000001011;
    Solution solu;
    int ans;
    ans = solu.hammingWeight(n);
    cout << ans <<endl;
    return 0;
}