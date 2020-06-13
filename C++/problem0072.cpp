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
    int minDistance(string word1, string word2) {
        // vector<int> dp {};
        // for ()
        // {
        //     vector<int> tmp {};
        //     for (int q = 0; q < word2.size()+1; ++q)
        //     {
        //         tmp.push_back(0)
        //     }
        //     dp.
        // }

        // vector<vector<int> > dp(word1.size()+1, vector<int>(word2.size()+1));
        vector<vector<int>> dp(word1.size()+1, vector<int>(word2.size()+1)); //>>没有空格也可以,只是看着不舒服
        // cout << dp.size();
        for (int k = 0; k < word2.size()+1; ++k)
        {
            dp[0][k] = k;
        }
        for (int k = 0; k < word1.size()+1; ++k)
        {
            dp[k][0] = k;
        }

        // for (int p = 0; p < dp.size(); ++p)
        // {
        //     for (int q = 0; q < dp[0].size(); ++q)
        //     {
        //         cout << dp[p][q] << '\t';
        //     }
        //     cout << endl;
        // }

        // system("pause");

        for (int p = 0; p < word1.size(); ++p)
        {
            for (int q = 0; q < word2.size(); ++q)
            {
                if (word1[p] == word2[q])
                {
                    dp[p+1][q+1] = dp[p][q];
                }
                else
                {
                    dp[p+1][q+1] = min(min(dp[p][q], dp[p][q+1]), dp[p+1][q]) + 1;
                    // dp[p+1][q+1] = min(dp[p][q], dp[p][q+1], dp[p+1][q]) + 1; //min()里面好像只能放两个数
                }
            }
        }

        // for (int p = 0; p < dp.size(); ++p)
        // {
        //     for (int q = 0; q < dp[0].size(); ++q)
        //     {
        //         cout << dp[p][q] << '\t';
        //     }
        //     cout << endl;
        // }

        return dp[word1.size()][word2.size()];
    }
};

int main()
{
    string word1 = "horse", word2 = "ros";
    Solution solu;
    int ans = solu.minDistance(word1, word2);
    cout << ans << endl;
    return 0;
}