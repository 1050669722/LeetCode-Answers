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
    int uniqueMorseRepresentations(vector<string>& words) {
        map<char, string> d;
        vector<string> morse {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        for (int k = 0; k < morse.size(); ++k)
        {
            d.insert(pair<char, string>((char)(k+97), morse[k]));
        }
        // cout << d.size() << endl;
        // cout << d['a'] << endl;
        // for (int k = 0; k<26; ++k)
        // {
        //     cout << d[(char)(k+97)] << endl;
        // }
        set<string> s;
        for (int p = 0; p < words.size(); ++p)
        {   
            string new_word;
            // cout << "new_word" << new_word << endl;
            for (int q = 0; q < words[p].size(); ++q)
            {   
                // cout << typeid(words[p][q]).name() << endl;
                // new_word.push_back(d[words[p][q]]);
                // new_word.push_back('a');
                // cout << "d[words[p][q]]" << d[words[p][q]] << endl;

                // if (new_word == "")
                // {
                //     new_word = d[words[p][q]];
                // }
                // else
                // {
                //     new_word.insert(new_word.end(), d[words[p][q]].begin(), d[words[p][q]].end());
                // }

                new_word.insert(new_word.end(), d[words[p][q]].begin(), d[words[p][q]].end());
                // cout << new_word << endl;
            }
            s.insert(new_word);
        }
        return s.size();
    }
};

int main()
{
    vector<string> words {"gin", "zen", "gig", "msg"};
    Solution solu;
    int ans = solu.uniqueMorseRepresentations(words);
    cout << ans << endl;

    // for (int k = 0; k < 26; ++k)
    // {
    //     cout << (char)(k+97) << endl;
    // }

    return 0;
}