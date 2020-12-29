class Solution {
public:
    void printMap(map<char, int> & m)
    {
        for (map<char, int>::iterator it = m.begin(); it != m.end(); ++it)
        {
            cout << "key = " << it->first << " value = " << it->second << endl;
        }
        cout << endl;
    }

    int firstUniqChar(string s) {
        map<char, int> m;
        for (string::iterator it = s.begin(); it < s.end(); ++it)
        {
            map<char, int>::iterator iter = m.find(*it);
            if (iter != m.end())
            {
                iter->second += 1;
            }
            else
            {
                m.insert(pair<char, int>(*it, 1));
            }
        }
        // printMap(m);

        for (string::iterator it = s.begin(); it < s.end(); ++it)
        {
            if (m[*it] == 1)
            {
                return it - s.begin();
            }
        }

        return -1;
    }
};
