class Solution {
public:
    bool isValid(string s) {
        map<char, char> m;
        // m.insert(pair<char, char>(')', '('));
        // m.insert(make_pair(')', '('));
        m.insert(map<char, char>::value_type(')', '('));
        // m[')'] = '(';
        m.insert(pair<char, char>(']', '['));
        m.insert(pair<char, char>('}', '{'));

        vector<char> v;
        // for (string::iterator it = s.rbegin(); it > s.rend(); --it)
        // {
        //     v.push_back(*it);
        // }

        for (string::iterator it = s.begin(); it < s.end(); ++it)
        {
            if (m.find(*it) != m.end())
            {
                if (!v.empty() && m[*it] == v.back()) //(v.size() != 0 && m[*it] == v.back())
                {
                    v.pop_back();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                v.push_back(*it);
            }
        }

        return v.empty();
    }
};
