#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

using namespace std;

int main()
{
    // // const int N = 100; //这里，N是常量
    // int N = 100; //此时，N是变量
    // int nums[N];
    // nums[0] = 9527;

    // cout << nums[0] << endl;

    // int months[12] = {1,3,5,7,8,10,12};
    // cout << months[8] << endl;

    // const int N = 5;
    // double scores[N];
    // cout << sizeof(scores)/sizeof(double) << endl;
    // cout << sizeof(scores) << endl;
    // for(int i=0; i<sizeof(scores)/sizeof(double); i++)
    // {
    //     cout << "please input the score of NO." << i+1 << " curriculum: ";
    //     cin >> scores[i];
    // }
    
    // for(int i=0; i<N; i++)
    // {
    //     cout << scores[i] << endl;
    // }

    // system("pause");

    int nums[] {8, 4, 2, 1, 23, 344, 12};
    int numsLen = sizeof(nums) / sizeof(int);
    int ans = 0;
    int Max = nums[0];
    int Min = nums[0];
    for (int i=0; i<numsLen; i++){
        ans += nums[i];
        if (nums[i] > Max){
            Max = nums[i];
        }
        else if (nums[i] < Min){
            Min = nums[i];
        }
    }

    // cout << ans << endl;  
    cout << ans << '\n'
         << ans / numsLen << '\n' 
         << Max << '\n'
         << Min << '\n'
         << endl;  

    return 0;
}