// class Solution {
// public:
//     double findMaxAverage(vector<int>& nums, int k) {
//         // if (k == 1)
//         // {
//         //     return *max_element(nums.begin(), nums.end()) / (double)k;
//         // }
        
//         vector<int>::iterator p = nums.begin(), q = p + k - 1;
//         double sum_ = accumulate(p, q, 0), max_ = sum_;
//         // cout << max_;
//         // cout << accumulate(p, q, 0) << endl;
//         // for (vector<int>::iterator it = nums.begin(); it < nums.end() - k + 1; ++it)
//         while (q < nums.end())
//         {
//             // cout << p - nums.begin() << ' ' << (q - 1) - nums.begin() << endl;
//             q++;
//             // if (q >= nums.end())
//             // {
//             //     break;
//             // }
//             // cout << max_ << ' ' << *p << ' ' << *(q - 1) << endl; 
//             sum_ = sum_ + *q - *p;
//             // cout << max_;
//             max_ = max(max_, sum_);
//             p++;   
//         }
//         return max_ / (double)k;
//     }
// };


class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int p = 0, q = p + k - 1;
        double sum_ = 0.;
        for (int i = p; i < q + 1; ++i)
        {
            sum_ += nums.at(i);
        }
        double max_ = sum_;
        
        while (q < nums.size())
        {
            q += 1;
            if (q == nums.size())
            {
                break;
            }
            sum_ = sum_ + nums.at(q) - nums.at(p);
            max_ = max(max_, sum_);
            p += 1;
        }

        return max_ / (double)k;

    }
};
