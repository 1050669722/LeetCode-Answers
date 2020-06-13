// #include <iostream>
// #include <iomanip>
// #include <cmath>
// #include <windows.h>
// #include <cstdlib>
// #include <ctime>
// #include <vector>
// #include <map>
// #include <algorithm>
// #include <unordered_map>

// using namespace std;

// // 1. Two Sum
// // https://leetcode.com/problems/two-sum/description/
// // 时间复杂度：O(n)
// // 空间复杂度：O(n)
// // class Solution {
// // public:
// //     // vector<int> twoSum(vector<int>& nums, int target) {
// //     vector<int> twoSum(vector<int>& nums, int target) {
// //         unordered_map<int,int> record;
// //         for(int i = 0 ; i < nums.size() ; i ++){
       
// //             int complement = target - nums[i];
// //             if(record.find(complement) != record.end()){
// //                 int res[] = {i, record[complement]};
// //                 return vector<int>(res, res + 2);
// //             }

// //             record[nums[i]] = i;
// //         }
// //     };
// // };
// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         map<int,int> a;//提供一对一的hash
//         vector<int> b(2,-1);//用来承载结果，初始化一个大小为2，值为-1的容器b
//         for(int i=0;i<nums.size();i++)
//         {
//             if(a.count(target-nums[i])>0)
//             {
//                 b[0]=a[target-nums[i]];
//                 b[1]=i;
//                 break;
//             }
//             a[nums[i]]=i;//反过来放入map中，用来获取结果下标
//         }
//         return b;
//     };
// };

// // // 作者：MisterBooo
// // // 链接：https://leetcode-cn.com/problems/two-sum/solution/dong-hua-tu-jie-suan-fa-liang-shu-zhi-he-fu-shi-pi/
// // // 来源：力扣（LeetCode）
// // // 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// int main()
// {
//     vector<int> nums = {2, 7, 11, 15};
//     int target = 9;
//     Solution solu;
//     vector<int> ans;
//     ans = solu.twoSum(nums, target);
//     vector<int>::iterator it;
//     for (it = ans.begin(); it != ans.end(); ++it)
//     {
//         cout << *it << '\t';
//     }
//     cout << endl;

//     return 0;
// }



// // #include <iostream>
 
// // using namespace std;
 
// // class Point
 
// // {
 
// //     private:
    
// //        int xPos;
 
// //        int yPos;

// //     public:
 
// //     void setPoint(int x, int y) //实现setPoint函数
    
// //     {
 
// //         xPos = x;
 
// //         yPos = y;
 
// //     }
 
 
// //     void printPoint() //实现printPoint函数
 
// //     {
 
// //         cout<< "x = " << xPos << endl;
 
// //         cout<< "y = " << yPos << endl;
 
// //     }
 
 
 
// // };
 
 
// // int main()
 
// // {
 
// //     Point M; //用定义好的类创建一个对象 点M
    
// //     M.setPoint(10, 20); //设置 M点 的x,y值
 
// //     M.printPoint(); //输出 M点 的信息
 
 
// //     return 0;
 
// // }


#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <windows.h>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

class Solution
{
    public:
        vector<int> twoSum(vector<int> nums, int target)
        {
            map<int, int> d;
            // vector<int> ans(2, -1);
            vector<int> ans;
            // vector<int>::iterator it;
            // for (it = nums.begin(); it != nums.end(); ++it)
            for (int k = 0; k < nums.size(); ++k)
            {
                if (d.count(target-nums[k])==1)
                {
                    // ans[0] = d[target-nums[k]];
                    // ans[1] = k;
                    // // return ans;
                    ans.push_back(d[target-nums[k]]);
                    ans.push_back(k);
                    break; 
                }
                else
                {
                    d[nums[k]] = k;
                }
            }
            return ans;
        };
};


int main()
{
    vector<int> nums {2, 7, 11, 15};
    int target = 9;
    Solution solu;
    vector<int> ans;
    ans = solu.twoSum(nums, target);
    vector<int>::iterator it;
    for (it = ans.begin(); it != ans.end(); ++it)
    {
        cout << *it << '\t';
    }
    cout << endl;

    return 0;
};



















