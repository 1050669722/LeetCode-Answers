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
    string longestPalindrome(string s) {
        string ans = "";

        if (s.empty())
        {
            return ans;
        }

        if (s.size() == 1)
        {
            return s;
        }

        if (s.size() == 2)
        {
            if (s[0] == s[1])
            {
                return s;
            }
            else
            {   
                ans.push_back(s[0]);
                return ans;
            }
        }

        if (s.size() == 3)
        {
            if (s[0] == s[2])
            {
                return s;
            }
            else if (s[0] == s[1])
            {
                ans.push_back(s[0]);
                ans.push_back(s[1]);
                return ans;
            }
            else if (s[1] == s[2])
            {
                ans.push_back(s[1]);
                ans.push_back(s[2]);
                return ans;
            }
            else
            {
                ans.push_back(s[0]);
                return ans;
            }
            
        }

        string::iterator it, tmp;

        //中心字符数量是奇数的情况
        for (it = s.begin()+1; it <= s.end()-2; ++it)
        {
            int k = 1;
            while (s.begin()<=it-k && it+k<=s.end()-1)
            {
                ans.push_back(*(it));
                if (*(it-k) == *(it+k))
                {
                    if (2*k+1 > ans.size())
                    {   
                        ans = "";
                        for (tmp = it-k; tmp <= it+k; ++tmp)
                        {   
                            ans.push_back(*tmp);
                        }
                    }
                    k++;
                }
                else
                {
                    break;
                }
            }
        }
        // string res1 = ans;
        // ans = "";
        // cout << res1 << endl;

        //中心字符数量是偶数的情况
        for (it = s.begin()+1; it <= s.end()-3; ++it)
        {   
            if (*(it)==*(it+1))
            {
                ans.push_back(*(it));
                ans.push_back(*(it+1));
                int k = 0;
                while (s.begin()<=it-k && it+1+k<=s.end()-1)
                {
                    if (*(it-k) == *(it+1+k))
                    {
                        if (2*k+2 > ans.size())
                        {   
                            ans = "";
                            for (tmp = it-k; tmp <= it+1+k; ++tmp)
                            {
                                ans.push_back(*tmp);
                            }
                        }
                        k++;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        // string res2 = ans;
        // cout << res2 << endl;

        // if (res1.size() > res2.size())
        // {
        //     return res1;
        // }
        // else
        // {
        //     return res2;
        // }

        return ans;

    }
};

int main()
{
    // string s = "babad";
    // string s = "aaaa";
    // string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    // string s = "eabcb";
    // string s = "abcda";
    string s = "aacdefcaa";
    // string s = "cbbd";
    // string s = "";
    // string s = "a";
    // string s = "aa";
    // string s = "ab";
    // string s = "aaa";
    // string s = "abb";
    // string s = "aab";
    Solution solu;
    string ans = solu.longestPalindrome(s);
    cout << ans << endl;
    return 0;
}