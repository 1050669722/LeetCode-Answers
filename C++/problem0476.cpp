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
    int findComplement(int num) {
        vector<int> tmp;
        int ans = 0;
        while (num)
        {
            tmp.push_back(num%2);
            num /= 2;
        }
        for (int k = 0; k < tmp.size(); ++k)
        {
            ans += (1-tmp[k]) * pow(2, k);
        }
        return ans;
    }
};

int main()
{
    int num = 5;
    Solution solu;
    int ans = solu.findComplement(num);
    cout << ans << endl;
    return 0;
}