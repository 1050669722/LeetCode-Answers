//代码中使用的 \texttt{pow}pow 函数的时空复杂度与 CPU 支持的指令集相关；

class Solution {
public:
    int climbStairs(int n) {
        // if (n == 1)
        // {
        //     return 1;
        // }
        // else if (n == 2)
        // {
        //     return 2;
        // }
        // return climbStairs(n - 1) + climbStairs(n - 2);

        vector<int> v{1, 2};
        for (int i = 2; i < n; ++i)
        {
            v.push_back(v[i - 1] + v[i - 2]);
        }
        // cout << n - 1 << ' ' << v.size() << endl;
        return v[n - 1];
        // return v[v.size() - 1];
    }
};
