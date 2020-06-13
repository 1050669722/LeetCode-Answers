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
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        map<int, int> d;
        for (int k = 0; k < B.size(); ++k)
        {
            d[B[k]] = k;
        }
        vector<int> ans; //如果这样定义，在添入元素之前就不能使用[]访问其中元素，因为其中还没有元素。
        for (int k = 0; k < A.size(); ++k)
        {
            ans.push_back(d[A[k]]);
            // A[k] = d[A[k]];
        }
        // cout << ans[0] << endl;
        return ans;
        // return A;
    }
};

int main()
{
    vector<int> A {12, 28, 46, 32, 50};
    vector<int> B {50, 12, 32, 46, 28};
    Solution solu;
    vector<int> ans = solu.anagramMappings(A, B);

    vector<int>::iterator it;
    for (it = ans.begin(); it != ans.end(); ++it)
    {
        cout << *it << '\t';
    }
    cout << endl;

    // for (int k = 0; k < ans.size(); ++k)
    // {
    //     cout << ans[k] << '\t';
    // }
    // cout << endl;

    return 0;
}