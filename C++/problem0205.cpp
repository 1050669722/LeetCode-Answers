class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s == t)
        {
            return true;
        }
        if (s.size() != t.size())
        {
            return false;
        }

        map<char, char> m;
        for (int i = 0; i < s.size(); ++i)
        {
            if (m.find(s[i]) == m.end())
            {
                // m.insert(pair<char, char>(s[i], t[i]));
                // m.insert(make_pair(s[i], t[i]));
                m.insert(map<char, char>::value_type(s[i], t[i]));
                m[s[i]] = t[i];
            }
            else
            {
                if (m[s[i]] != t[i])
                {
                    return false;
                }
            }
        }

        m.clear();
        for (int i = 0; i < s.size(); ++i)
        {
            if (m.find(t[i]) == m.end())
            {
                m.insert(pair<char, char>(t[i], s[i]));
            }
            else
            {
                if (m[t[i]] != s[i])
                {
                    return false;
                }
            }
        }

        return true;
    }
};
