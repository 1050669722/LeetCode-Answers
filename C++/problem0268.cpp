// class Solution {
// public:
//     int missingNumber(vector<int>& nums) {
//         int accumulation = 0, size_ = 0;
//         for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
//         {
//             accumulation += *it;
//             size_++;
//         }
//         return (0 + size_) * (size_ + 1) / 2 - accumulation;
//     }
// };


class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = nums.size();
        for (vector<int>::iterator it = nums.begin(); it < nums.end(); ++it)
        {
            ans ^= *it ^ (it - nums.begin());
        }
        return ans;
    }
};
