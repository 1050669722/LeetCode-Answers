class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        if (A.size() == 1)
        {
            return true;
        }

    //     if (A[0] <= A[1])
    //     {
    //         for (vector<int>::iterator it = ++A.begin(); it < A.end(); ++it)
    //         {
    //             if (*it - *(it - 1) < 0)
    //             {
    //                 return false;
    //             }
    //         }
    //         return true;
    //     }

    //     else
    //     {
    //         for (vector<int>::iterator it = ++A.begin(); it < A.end(); ++it)
    //         {
    //             if (*it - *(it - 1) > 0)
    //             {
    //                 return false;
    //             }
    //         }
    //         return true;
    //     }
    // }

        set<int> tmp;
        for (vector<int>::iterator it = ++A.begin(); it < A.end(); ++it)
        {
            if (*it - *(it - 1) > 0)
            {
                tmp.insert(1);
            }
            else if(*it - *(it - 1) == 0)
            {
                tmp.insert(0);
            }
            else
            {
                tmp.insert(-1);
            }
            
        }
        if (tmp.find(1) != tmp.end() && tmp.find(-1) != tmp.end())
        {
            return false;
        }
        return true;

    }
};
