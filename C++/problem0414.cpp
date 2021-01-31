class Solution {
public:
    int thirdMax(vector<int>& nums) {
        // sort(nums.begin(), nums.end());

        set<int> s;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            s.insert(*it);
        }
        
        if (s.size() < 3)
        {
            int max_ = nums[0];
            for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
            {
                if (*it > max_)
                {
                    max_ = *it;
                }
            }
            return max_;
        }

        // vector<int>::iterator it = nums.end();
        // return *(it - 3);

        int First = INT_MIN, Second = INT_MIN, Third = INT_MIN;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            if (*it == First || *it == Second || *it == Third)
            {
                continue;
            }
            if (*it > First)
            {
                Third = Second;
                Second = First;
                First = *it;
            }
            else if (*it > Second)
            {
                Third = Second;
                Second = *it;
            }
            else if (*it > Third)
            {
                Third = *it;
            }
        }
        return Third;
    }
};
