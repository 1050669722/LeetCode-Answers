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
    string reverseWords(string s) {
        string stack, ans;
        // cout << boolalpha;
        while (s.empty() == false)
        // while (!s.empty())
        {
            // char tmp = s[s.size()-1];
            char tmp = *(s.end()-1);
            s.pop_back();
            if (tmp != ' ')
            {
                stack.push_back(tmp);
            }
            else
            {
                ans.insert(ans.begin(), stack.begin(), stack.end());
                string temp = " ";
                ans.insert(ans.begin(), temp.begin(), temp.end());
                stack = "";
            }
        }
        ans.insert(ans.begin(), stack.begin(), stack.end());
        return ans;
    }
};

int main()
{
    string s = "Let's take LeetCode contest";
    Solution solu;
    string ans = solu.reverseWords(s);
    cout << ans << endl;
    return 0;
}