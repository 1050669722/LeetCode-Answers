class Solution {
public:
    void printVector(const vector<int> & v)
    {
        for (vector<int>::const_iterator it = v.begin(); it < v.end(); ++it)
        {
            cout << *it << ' ';
        }
        cout << endl;
        return;
    }

    int equalSubstring(string s, string t, int maxCost) {
        vector<int> diff;
        for (int i = 0; i < s.size(); ++i)
        {
            diff.push_back(abs(s.at(i) - t[i]));
        }
        // printVector(diff);

        int left = 0, right = 0;
        int sum_ = 0, length = 0;

        while (right < s.size())
        {
            sum_ += diff.at(right);
            while (sum_ > maxCost)
            {
                sum_ -= diff[left];
                left += 1;
            }
            length = max(right - left + 1, length);
            right += 1;
        }

        return length;
    }
};
