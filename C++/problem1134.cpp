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

class Solution
{
    public:
        bool isArmstrong(int N)
        {
            vector<int> Num;
            int Sum = 0;
            int n = N;
            while (n)
            {
                // cout << n%10 << endl;
                Num.push_back(n%10);
                n /= 10;
            }
            int p = Num.size();
            // cout << p << endl;
            for (int k = 0; k < Num.size(); ++k)
            {
                cout << Sum << endl;
                cout << pow(Num[k], p) << endl;
                int tmp = pow(Num[k], p);
                cout << typeid(tmp).name() << endl;
                Sum += tmp;
                // Sum = Sum + pow(Num[k], p);
                cout << "***" << Sum << "***" << endl;
            }
            // cout << Sum << endl;
            cout << "===" << 27+125 << "===" << endl;
            return Sum == N;
        }
};


// class Solution {
// public:
//     bool isArmstrong(int N) 
//     {
//         string tmp=to_string(N);
//         int n=tmp.length();
//         int res=0;
//         for(int i=0;i<n;i++)
//         {
//             int val=tmp[i]-'0';
//             res+=pow(val,n);
//         }
//         return res==N;
//     }
// };

int main()
{
    int N = 153;
    Solution solu;
    bool ans = solu.isArmstrong(N);
    cout << ans << endl;
    return 0;
}