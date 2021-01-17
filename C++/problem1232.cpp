class Solution {
public:
    void printSet0(set<int> & x)
    {
        for (set<int>::iterator it = x.begin(); it != x.end(); ++it)
        {
            cout << *it << ' ';
        }
        cout << endl;
    }

    void printSet1(set<float> & x)
    {
        for (set<float>::iterator it = x.begin(); it != x.end(); ++it)
        {
            cout << *it << ' ';
        }
        cout << endl;
    }

    bool checkStraightLine(vector<vector<int>>& coordinates) {
        set<int> s;
        for (vector<vector<int>>::iterator it = coordinates.begin(); it < coordinates.end(); ++it)
        {
            s.insert((*it).front());
        }

        // printSet0(s);

        if (s.size() == 1)
        {
            return true;
        }

        set<float> t;
        for (vector<vector<int>>::iterator it = coordinates.begin() + 1; it < coordinates.end(); ++it)
        {
            if ((*(it)).front() == (*(it - 1)).front())
            {
                return false;
            }
            // cout << (float)(((*(it)).back() - (*(it - 1)).back()) / ((*(it)).front() - (*(it - 1)).front())) << endl;
            t.insert((float)((*(it)).back() - (*(it - 1)).back()) / (float)((*(it)).front() - (*(it - 1)).front()));
        }

        // printSet1(t);

        return t.size() == 1;
    }
};
