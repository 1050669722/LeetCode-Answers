#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <windows.h>

using namespace std;

int main()
{
    // //两种方式声明数组
    // int num[5];
    // int* nums = new int[5]; //在堆内存中分配了5个整型空间
    // cout << sizeof(num) << '\t' << sizeof(nums) << endl;
    // delete nums;
    // // delete num;

    int* ptr = new int;
    *ptr = 90;
    int* ptr1 = ptr;
    // delete ptr;
    cout << *ptr << endl;

    return 0;
}