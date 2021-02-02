class Solution {
public:
    int characterReplacement(string s, int k) {
        map<int, int> m;
        // for (string::iterator it = s.begin(); it < s.end(); ++it)
        // {
        //     if (m.find(*it) == m.end())
        //     {
        //         m[*it] = 1;
        //     }
        //     else
        //     {
        //         m[*it]++;
        //     }
        // }

        string::iterator p = s.begin(), q = s.begin();
        int maxn = 0;
        while (q < s.end())
        {
            m[*q] += 1;
            maxn = max(maxn, m[*q]);
            if (q - p + 1 - maxn > k)
            {
                m[*p] -= 1;
                p++;
            }
            q++;
        }

        return q - p;
    }
};
