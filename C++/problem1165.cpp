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
    int calculateTime(string keyboard, string word) {
        map<char, int> d;
        for (int k = 0; k < keyboard.size(); ++k)
        {
            // d.insert(pair<char, int>(keyboard[k], k));
            d[keyboard[k]] = k; //两种插入键值对的方式都可以
        }
        int ans = d[word[0]] - 0;
        for (int k = 1; k < word.size(); ++k)
        {
            // int tmp = d[word[k]] - d[word[k-1]];
            // ans += abs(tmp);
            ans += abs(d[word[k]] - d[word[k-1]]);
        }
        return ans;
    }
};

int main()
{
    string keyboard = "abcdefghijklmnopqrstuvwxyz";
    string word = "cba";
    Solution solu;
    int ans = solu.calculateTime(keyboard, word);
    cout << ans << endl;
    return 0;
}