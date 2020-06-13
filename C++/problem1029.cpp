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
    int twoCitySchedCost(vector<vector<int>>& costs) {
        sort(costs.begin(), costs.end(), 
                [](vector<int> o1, vector<int> o2) //这像一个匿名函数 没有函数名和返回类型
                {
                    return (o1[0]-o1[1] < o2[0]-o2[1]);                    
                }
        );
        int n = costs.size()/2; //两个整型自动就是整除，不需要强制类型转换 int n = (int)costs.size()/2;
        // int n = costs.size()/2.0; //可能有隐式转换
        int ans = 0;
        for (int k = 0; k < n; ++k)
        {
            ans += costs[k][0] + costs[k+n][1];
        }
        return ans;
    }
};

int main()
{
    //costs中的临时向量可能不需要名称
    vector<vector<int>> costs {vector<int> {10, 20}, vector<int> {30, 200}, vector<int> {400, 50}, vector<int> {30, 20}};
    Solution solu;
    int ans = solu.twoCitySchedCost(costs);
    cout << ans << endl;
    return 0;
}