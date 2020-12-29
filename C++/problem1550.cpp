class Solution {
public:
    bool isOdd(int n)
    {
        if (n % 2 != 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    bool threeConsecutiveOdds(vector<int>& arr) {
        int tmp = 0;
        for (vector<int>::iterator it = arr.begin(); it < arr.end(); ++it)
        {
            if (isOdd(*it))
            {
                tmp += 1;
            }
            else
            {
                tmp = 0;
            }

            if (tmp == 3)
            {
                return true;
            }
        }
        return false;
    }
};
