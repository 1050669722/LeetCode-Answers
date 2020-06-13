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
    int surfaceArea(vector<vector<int>>& grid) {
        int ans = 0;
        for (int p = 0; p < grid.size(); ++p)
        {
            for (int q = 0; q < grid[0].size(); ++q)
            {
                if (grid[p][q] > 0)
                {

                    ans += 2;

                    if (p != 0)
                    {
                        ans += max(0, grid[p][q]-grid[p-1][q]);
                    }
                    else
                    {
                        ans += grid[p][q];
                    }

                    if (p != grid.size()-1)
                    {
                        ans += max(0, grid[p][q]-grid[p+1][q]);
                    }
                    else
                    {
                        ans += grid[p][q];
                    }

                    if (q != 0)
                    {
                        ans += max(0, grid[p][q]-grid[p][q-1]);
                    }
                    else
                    {
                        ans += grid[p][q];
                    }

                    if (q != grid[0].size()-1)
                    {
                        ans += max(0, grid[p][q]-grid[p][q+1]);
                    }
                    else
                    {
                        ans += grid[p][q];
                    }
                
                }
                
                
            }
        }
        return ans;
    }
};

int main()
{
    vector<vector<int>> grid {{1,1,1},{1,0,1},{1,1,1}};
    Solution solu;
    int ans = solu.surfaceArea(grid);
    cout << ans << endl;
    return 0;
}