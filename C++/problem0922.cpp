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
    vector<int> sortArrayByParityII(vector<int>& A) {
        int j = 1;
        for (int i = 0; i < A.size(); i += 2)
        {
            if (A[i]%2 == 1)
            {
                while (A[j]%2 == 1)
                    {
                        j += 2;
                    }
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }
        }
        return A;
    }
};

int main()
{
    vector<int> A {4,2,5,7};
    Solution solu;
    vector<int> ans = solu.sortArrayByParityII(A);
    vector<int>::iterator it;
    for (it = ans.begin(); it < ans.end(); ++it)
    {
        cout << *it << '\t';
    }
    cout << endl;
    return 0;
}
