#include <numeric>

class Solution {
public:
    int isupper(char x)
    {
        if ('A' <= x && x <= 'Z')
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    // int islower(char x)
    // {
    //     if ('a' <= x && x <= 'z')
    //     {
    //         return 0;
    //     }
    //     else
    //     {
    //         return 1;
    //     }
    // }

    bool detectCapitalUse(string word) {
        vector<int> v;
        for (string::iterator it = word.begin(); it < word.end(); ++it)
        {
            v.push_back(isupper(*it));
        }
        
        // for (int i = 0; i < v.size(); ++i)
        // {
        //     cout << v[i] << ' ';
        // }
        // cout << endl;

        int sumv = accumulate(v.begin(), v.end(), 0);
        // cout << sumv << endl;
        if (sumv == word.size() || sumv == 0)
        {
            return true;
        }
        else if (sumv == 1 && v.front() == 1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
