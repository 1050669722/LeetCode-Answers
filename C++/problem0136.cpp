// class Solution {
// public:
//     void printMap(map<int, int> & m)
//         {
//             for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it)
//                 {
//                     cout << "key = " << it->first << " value = " << it->second << endl;
//                 }
//             cout << endl;
//         }

//     int singleNumber(vector<int>& nums) {
//         map<int, int> m;
//         for (vector<int>::iterator it = nums.begin(); it != nums.end(); ++it)
//         {
//             map<int, int>::iterator iter = m.find(*it);
//             if (iter != m.end())
//             {
//                 // (*iter).second += 1;
//                 iter->second++;
//             }
//             else
//             {
//                 m.insert(pair<int, int>(*it, 1));
//             }
//         }

//         // cout << "测试" << endl;
//         // printMap(m);

//         for (map<int, int>::iterator it = m.begin(); it != m.end(); ++it)
//         {
//             // cout << it->second << endl;
//             if (it->second == 1)
//             {
//                 return it->first;
//             }
//         }

//     return 0;
//     }
// };


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ret = 0;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            ret ^= *it;
        }
        return ret;
    }
};
