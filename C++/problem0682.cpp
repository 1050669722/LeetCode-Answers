#include <iostream>
#include <string>
#include <cstring>
#include <numeric>

using namespace std;

class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> v;
        // int flag = 0;
        for (vector<string>::iterator it = ops.begin(); it < ops.end(); ++it)
        {
            // flag++;
            // if (flag > 1)
            // {
            //     cout << *(it - 1) << ' ';
            //     // ++it;
            // }
            
            if (*it == "C") //字符串比较
            {
                v.pop_back();
            }
            else if (*it == "D")
            {
                v.push_back(2 * v.back());
            }
            else if ((*it).compare("+") == 0) //字符串比较
            {
                // v.push_back(v[v.size() - 1] + v[v.size() - 2]);
                v.push_back(*(v.end() - 1) + *(v.end() - 2));
                // cout << *(it - 1);
                // cout << stoi(*(it - 1)) << ' '; //v 和 s 得区分
            }
            else
            {
                // cout << stoi(*it) << ' ';
                v.push_back(stoi(*it)); //字符串转整型
            }
        }
        return accumulate(v.begin(), v.end(), 0); //vector求和
    }
};

