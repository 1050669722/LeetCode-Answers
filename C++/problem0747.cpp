class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        if (nums.size() == 1)
        {
            return 0;
        }
        
        int First = INT_MIN, Second = INT_MIN, first = -1/*, second = -1*/;
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            if (*it > First)
            {
                Second = First/*, second = first*/;
                First = *it, first = it - nums.begin();
            }
            else if (*it > Second)
            {
                Second = *it/*, second = it - nums.begin()*/;
            }
        }

        if (First >= Second * 2)
        {
            return first;
        }
        else
        {
            return -1;
        }
    }
};
