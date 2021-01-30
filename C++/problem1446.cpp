// class Solution {
// public:
//     int maxPower(string s) {
//         char tmp = '\0';
//         int ans = 0;
//         vector<int> res;
//         for (string::iterator it = s.begin(); it < s.end(); ++it)
//         {
//             // cout << tmp << endl;
//             if (tmp == '\0' || tmp != *it)
//             {
//                 tmp = *it;
//                 res.push_back(ans);
//                 ans = 1;
//             }
//             else
//             {
//                 ans++;
//             }
//         }
//         res.push_back(ans);

//         return *max_element(res.begin(), res.end());
//     }
// };


class Solution {
public:
    int maxPower(string s) {
        if (s.size() == 1)
        {
            return 1;
        }

        char lastchar = s[0];
        int ans = 1, num = 1;
        for (string::iterator it = ++s.begin(); it < s.end(); ++it)
        {
            if (*it == lastchar)
            {
                num++;
            }
            else
            {
                ans = max(ans, num);
                lastchar = *it;
                num = 1;
            }
        }
        ans = max(ans, num);

        return ans;
    }
};
