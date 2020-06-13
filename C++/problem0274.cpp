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

bool cmp(int a, int b)
{
    return a>b;
}

class Solution {
public:
    int hIndex(vector<int>& citations) {
        if (citations.size() == 0)
        {
            return 0;
        }
        
        sort(citations.begin(), citations.end(), cmp);
        map<int, int> d;
        d[citations[0]] = 1;
        for (int k = 1; k < citations.size(); ++k)
        {
            if (d.count(citations[k]) != 0)
            {
                d[citations[k]]++;
            }
            else
            {
                d[citations[k]] = k + 1;
            }
        }
        int ans= 0;
        map<int, int>::iterator iter;
        for (iter = d.begin(); iter != d.end(); ++iter)
        {
            ans = max(ans, min(iter->first, iter->second));
        }
        return ans;
    }
};

int main()
{
    vector<int> citations {3,0,6,1,5};
    Solution solu;
    int ans = solu.hIndex(citations);
    cout << ans << endl;
    return 0;
}