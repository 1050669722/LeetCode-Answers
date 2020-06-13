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
};

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end(), cmp);
        int p = 0, q = people.size()-1;
        int ans = 0;
        while (p <= q)
        {
            ans += 1;
            if (people[p] + people[q] > limit)
            {
                p += 1;
            }
            else
            {
                p += 1;
                q -= 1;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> people = {1, 2}; 
    int limit = 3;
    // vector<int> people {3,2,2,1}; 
    // int limit = 3;
    // vector<int> people {3,5,3,4};
    // int limit = 5;
    Solution solu;
    int ans = solu.numRescueBoats(people, limit);
    cout << ans << endl;
    return 0;
}