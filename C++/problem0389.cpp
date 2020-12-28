// class Solution {
// public:
//     char findTheDifference(string s, string t) {
//         map<char, int> m;
//         for (int i = 0; i < s.size(); ++i)
//         {
//             map<char, int>::iterator it = m.find(s[i]);
//             if (it != m.end())
//             {
//                 it->second++;
//             }
//             else
//             {
//                 m.insert(pair<char, int>(s[i], 1));
//             }
//         }
        
//         for (int i = 0; i < t.size(); ++i)
//         {
//             map<char, int>::iterator it = m.find(t[i]);
//             if (it != m.end() && it->second > 0)
//             {
//                 it->second--;
//             }
//             else
//             {
//                 return t[i];
//             }
//         }
        
//         return ' ';
//     }
// };

// class Solution {
// public:
//     char findTheDifference(string s, string t) {
//         int ret = 0;
//         for (int i = 0; i < s.size(); ++i)
//         {
//             ret ^= s[i];
//         }
//         for (int i = 0; i < t.size(); ++i)
//         {
//             ret ^= t[i];
//         }
//         return ret; //出现奇数次的元素
//     }
// };

// class Solution {
// public:
//     char findTheDifference(string s, string t) {
//         int sum_s = 0, sum_t = 0;
//         for (int i = 0; i < s.size(); ++i)
//         {
//             sum_s += s[i];
//         }
//         cout << (char)sum_s << endl; //强制类型转换
//         for (int i = 0; i < t.size(); ++i)
//         {
//             sum_t += t[i];
//         }

//         return sum_t - sum_s; //这里有一个隐式的强制类型转换
//     }
// };

class Solution {
public:
    void printVec(vector<int> & v)
    {
        for (vector<int>::iterator it = v.begin(); it < v.end(); ++it)
        {
            cout << *it << ' ';
        }
        cout << endl;
        return;
    }

    char findTheDifference(string s, string t) {
        vector<int> v(26, 0);
        // vector<int> v;
        // v.assign(26, 0);
        // printVec(v);
        for (int i = 0; i < s.size(); ++i) //还是把类型强制转换显式地表达出来比较好
        {
            // cout << i << ' ' << (int)(s[i] - 'a') << endl;
            v[(int)(s[i] - 'a')] += 1;
        }
        for (int i = 0; i < t.size(); ++i)
        {
            v[(int)(t[i] - 'a')] -= 1;
            if (v[(int)(t[i] - 'a')] < 0)
            {
                return t[i];
            }
        }

        return ' ';
    }
};
