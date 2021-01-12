class Solution {
public:
    bool isPalindrome(string s) {
        if (s.size() == 0)
        {
            return true;
        }

        vector<char> v;
        for (int i = 0; i < s.size(); ++i)
        {
            if (isalnum(s[i]))
            {
                v.push_back(s[i]);
                // cout << s[i] << ' ';
            }
        }


        int i = 0, j = v.size() - 1;
        while (i < j)
        {
            // cout << v[i] << ' ' << v[j] << endl;
            if (toupper(v[i]) != toupper(v[j]))
            // if (strupr(v[i]) != strupr(v[j]))
            {
                return false;
            }
            i++, j--;
        }

        // vector<char>::iterator it_i = v.begin(), it_j = v.end() - 1;
        // cout << *it_i << ' ' << *it_j << endl;
        // while (it_i < it_j)
        // {
        //     if (toupper(*it_i) != toupper(*it_j))
        //     {
        //         return false;
        //     }
        //     it_i++, it_j--;
        // }

        
        return true;
    }
};
