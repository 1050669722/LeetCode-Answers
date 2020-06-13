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
    //int* int[] 都是类型 //一定得是3吗？ //相当于int[5]被(*ptr)代替。5个一维数组。
    int(* ptr)[3] = new int[5][3]; //降维 指针类型的数组。 int(* ptr)[5] = new int[5][3];
    //此时的ptr是一个指针，指向最高维的首地址，ptr平移之后可以遍历下一维的所有首地址，最高维看成一个一位数组；相当于int[5]被(*ptr)代替
    // cout << sizeof(ptr) << endl;
    ptr[3][2] = 998;
    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            // cout << ptr[i][j] << ',' << '\t';
            cout << *(*(ptr+i)+j) << ',' << '\t';//这里的ptr+k表示地址//所以这是相当于一个地址嵌套递归，直到最外层，才取出值，中间的取的值仍然表示地址。
        }
        cout << endl;
    }
    delete ptr;

    // int* ptr = new int[5];
    // // cout << ptr << endl;
    // ptr[0] = 10; //数组本身很特殊，不是单个变量那样，有时候表示首地址（打印、赋值），但是在这里表示数组本身。
    // for (int k = 0; k < 5; ++k)
    // {
    //     cout << ptr[k] << endl;
    // }
    // delete ptr;

    return 0;
}