// class Solution {
// public:
//     static bool cmp(int a, int b)
//     {
//         return a > b;
//     }

//     int maxProduct(vector<int>& nums) {
//         sort(nums.begin(), nums.end(), cmp);
//         return (nums[0] - 1) * (nums[1] - 1);
//     }
// };

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max = nums[0], submax = 1;
        // vector<int>::iterator test = nums.begin() + 2;
        for (vector<int>::iterator it = ++nums.begin(); it < nums.end(); ++it) //有些迭代器不能做加法的原因是不支持，底层数据结构不支持那样的操作（这些数据结构不是实现在内存中不是连续的，所以不是RA[随机访问]的），可能并不是类型尺寸的问题；
        {
            if (*it > max)
            {
                submax = max;
                max = *it;
            }
            else if (*it <= max && *it > submax)
            {
                submax = *it;
            }
        }
        return (max - 1) * (submax - 1);
    }
};
