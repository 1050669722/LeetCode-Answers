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
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        for (int k = 0; k < A.size(); ++k)
        {
            int p = 0, q = A[k].size()-1;
            while (p <= q)
            {
                if (p == q)
                {
                    A[k][p] = 1 - A[k][p];
                    break;
                }
                int tmp = A[k][p];
                A[k][p] = A[k][q];
                A[k][q] = tmp;
                A[k][p] = 1 - A[k][p];
                A[k][q] = 1 - A[k][q];
                p++;
                q--;
            }
        }
        return A;
    }
};

int main()
{
    vector<vector<int>> A {{1,1,0},{1,0,1},{0,0,0}};
    Solution solu;
    vector<vector<int>> ans = solu.flipAndInvertImage(A);
    for (int p = 0; p < A.size(); ++p)
    {
        for (int q = 0; q < A[0].size(); ++q)
        {
            cout << A[p][q] << '\t';
        }
        cout << endl;
    }
    cout << endl;
    return 0;
}