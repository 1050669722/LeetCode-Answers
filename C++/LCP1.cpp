#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <windows.h>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

class Solution {
public:
    int game(vector<int>& guess, vector<int>& answer) {
        int ans = 0;
        for (int k = 0; k < guess.size(); ++k)
        {
            if (guess[k] == answer[k])
            {
                ans += 1;
            }
        }
        return ans;
    }
};

int main()
{
    vector<int> guess {1, 2, 3};
    vector<int> answer {1, 2, 3};
    Solution solu;
    int ans;
    ans = solu.game(guess, answer);
    cout << ans << endl;

    return 0;
}