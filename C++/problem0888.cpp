class Solution {
public:
    vector<int> fairCandySwap(vector<int>& A, vector<int>& B) {
        int diff = accumulate(A.begin(), A.end(), 0) - accumulate(B.begin(), B.end(), 0);
        // cout << diff << endl;

        vector<int> ans;
        
        map<int, int> m;
        for (vector<int>::iterator it = B.begin(); it < B.end(); ++it)
        {
            m.insert(make_pair(*it, it - B.begin()));
        }

        for (vector<int>::iterator it = A.begin(); it < A.end(); ++it)
        {
            // cout << diff / 2 << *it << endl;
            if (m.count(*it - diff / 2) != 0)
            {
                // return vector<int>{(int)(it - A.begin()), m[diff / 2 - *it]};
                return vector<int>{*it, *it - diff / 2};
            }
        }

        return vector<int>{};
    }
};
