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
    bool judgeCircle(string moves) {
        map<char, int> d;
        d.insert(pair<char, int>('L', 0));
        d.insert(pair<char, int>('R', 0));
        d.insert(pair<char, int>('U', 0));
        d.insert(pair<char, int>('D', 0));
        for (int k = 0; k < moves.size(); ++k)
        {
            d[moves[k]] += 1;
        }
        return d['L'] == d['R'] and d['U'] == d['D'];
    }
};

int main()
{
    // string moves = "UD";
    string moves = "LL";
    Solution solu;
    bool ans = solu.judgeCircle(moves);
    cout << ans << endl;
    return 0;
}