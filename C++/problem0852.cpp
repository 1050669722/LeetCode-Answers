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

// class Solution {
// public:
//     int peakIndexInMountainArray(vector<int>& A) {
//         if (A.empty())
//         {
//             return NULL;
//         }
//         //前向差分
//         vector<int>::iterator it;
//         for (it = A.begin()+1; it != A.end(); ++it)
//         {
//             if ( *(it-1)<*(it) && *(it)>*(it+1) )
//             {
//                 return it - A.begin();
//             }
//         }
//         return NULL;
//         // for (int k = 1; k < A.size(); ++k)
//         // {
//         //     if ( A[k-1]<A[k] && A[k]>A[k+1] )
//         //     {
//         //         return k;
//         //     }
//         // }
//         // return NULL
//     }
// };

// class Solution {
// public:
//     int peakIndexInMountainArray(vector<int>& A) {
//         if (A.empty())
//         {
//             return NULL;
//         }
//         //最大值
//         vector<int>::iterator biggest = max_element(A.begin(), A.end());
// //      return biggest - A.begin();
//         return distance(A.begin(), biggest);
//     }
// };

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        // if (A.empty())
        // {
        //     return NULL;
        // }
        //二分查找
        int p = 0, q = A.size()-1, k;
        while (p < q)
        {
            k = (p+q)/2;
            cout << p << '\t' << q << '\t' << k << endl;
            if (A[k-1]<A[k] && A[k]<A[k+1])
            {
                p = k + 1;
            }
            else if (A[k-1]>A[k] && A[k]>A[k+1])
            {
                q = k - 1;
            }
            else
            {
                return k;
            }  
        }
        return p;
    }
};

int main()
{
    // vector<int> A {0,2,1,0};
    vector<int> A {0,10,5,2};
    Solution solu;
    /*void*/ int ans = solu.peakIndexInMountainArray(A);
    cout << ans << endl;
    return 0;
}