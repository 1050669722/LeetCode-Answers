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

// class Solution {
// public:
//     void reverseString(vector<char>& s) {
//         // sort(s.begin(), s.end());
//         reverse(s.begin(), s.end());
//     }
// };

class Solution {
public:
    void reverseString(vector<char>& s) {
        if (s.size()>0)
        {
            vector<char>::iterator p;
            vector<char>::iterator q;
            p = s.begin();
            q = s.end()-1;
            // cout << "t: ";
            // char a = s[s.size()]; 
            // cout << (a == '\0') << endl;
            // cout << (s[s.size()] == '\0') << endl;
            // vector<char>::iterator t;
            // t = s.end();
            // cout << (*t == '\0') << endl;
            // cout << a << '\t' << (a == '\0') << endl;
            // cout << '|' << *t << '|' << endl;
            while (p < q)
            {
                char tmp = *p;
                *p = *q;
                *q = tmp;
                p++;
                q--;
            }
        }
    }
};

int main()
{
    vector<char> s {'h','e','l','l','o'};
    // vector<char> s {"h","e","l","l","o"}; //这样写是不可以的；严格区分字符和字符串。
    // char s[] {'h','e','l','l','o'};
    Solution solu;
    solu.reverseString(s);
    for (int k = 0; k < s.size(); ++k)
    {
        cout << s[k] << '\t';
    }
    cout << endl;
    return 0;
}