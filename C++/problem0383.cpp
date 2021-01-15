// class Solution {
// public:
//     map<char, int> count(string s)
//     {
//         map<char, int> m;
//         for (string::iterator it = s.begin(); it < s.end(); ++it)
//         {
//             if (m.find(*it) != m.end())
//             {
//                 m[*it] += 1;
//             }
//             else
//             {
//                 m.insert(pair<char, int>(*it, 1));
//             }
//         }
//         return m;
//     }

//     bool canConstruct(string ransomNote, string magazine) {
//         map<char, int> m1 = count(ransomNote), m2(count(magazine)); //这样初始化，不用等号的初始化也是可以的 = () assign

//         for (map<char, int>::iterator it = m1.begin(); it != m1.end(); ++it)
//         {
//             // cout << it->first << endl;
//             if (m2.find(it->first) == m2.end())
//             {
//                 return false;
//             }
//             // cout << it->first << endl;
//             // cout << (*it).first << endl;
//             // cout << m2["a"[0]] << endl;
//             if (m2[it->first] < (*it).second)
//             {
//                 return false;
//             }
//         }

//         return true;
//     }
// };


class Solution {
public:
    map<char, int> count(string s)
    {
        map<char, int> m;
        for (string::iterator it = s.begin(); it < s.end(); ++it)
        {
            if (m.find(*it) != m.end())
            {
                m[*it] += 1;
            }
            else
            {
                m.insert(pair<char, int>(*it, 1));
            }
        }
        return m;
    }

    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> m(count(magazine));
        for (string::iterator it = ransomNote.begin(); it < ransomNote.end(); ++it)
        {
            m[*it] -= 1;
        }
        for (map<char, int>::iterator it = m.begin(); it != m.end(); ++it)
        {
            if (it->second < 0)
            {
                return false;
            }
        }
        return true;
    }
};
