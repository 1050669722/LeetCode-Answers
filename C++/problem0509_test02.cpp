// class Solution {
// public:
//     int fib(int n) {
//         if (n == 0 || n == 1)
//         {
//             return n;
//         }
//         else
//         {
//             return fib(n - 1) + fib(n - 2);
//         }
//     }
// };


// class Solution {
// public:
//     int fib(int n) {
//         if (n == 0 || n == 1)
//         {
//             return n;
//         }
//         vector<int> v;
//         v.push_back(0);
//         v.push_back(1);
//         vector<int>::iterator it;
//         for (int i = 2; i < n + 1; ++i)
//         {
//             it = v.end();
//             v.push_back(*--it + *--it);
//         }
//         return v.back();
//     }
// };


class Solution {
public:
    int fib(int n) {
        if (n == 0 || n == 1)
        {
            return n;
        }

        int a = 0, b = 1;

        for (int i = 2; i < n + 1; ++i)
        {
            // int tmp = a + b;
            // a = b;
            // b = tmp;

            b += a;
            a = b - a;
        }

        return b;

    }
};
