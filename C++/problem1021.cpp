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
    string removeOuterParentheses(string S) {
        int mark = 0;
        // vector<char> stack;
        string stack; //string 和 vector比较像
        for (int k = 0; k < S.size(); ++k)
        {
            if (S[k] == '(')
            {
                if (mark != 0)
                    stack.push_back(S[k]);
                mark += 1;
            }
            else
            {
                mark -= 1;
                if (mark != 0)
                    stack.push_back(S[k]);
            }
        }
        return stack;
    }
};

int main()
{
    string S = "(()())(())";
    Solution solu;
    string ans = solu.removeOuterParentheses(S);
    cout << ans << endl;
    return 0;
}