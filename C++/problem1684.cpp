class Solution {
public:
    int isAllowed(string & x, set<char> & a)
    {
        for (string::iterator it = x.begin(); it < x.end(); ++it)
        {
            if (a.find(*it) == a.end())
            {
                return 0;
            }
        }
        return 1;
    }

    int countConsistentStrings(string allowed, vector<string>& words) {
        set<char> s;
        for (string::iterator it = allowed.begin(); it < allowed.end(); ++it)
        {
            s.insert(*it);
        }

        int ans = 0;
        for (vector<string>::iterator it = words.begin(); it < words.end(); ++it)
        {
            ans += isAllowed(*it, s);
        }

        return ans;
    }
};
