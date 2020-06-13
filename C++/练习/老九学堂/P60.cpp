#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib> //这里面包含NULL
#include <windows.h>

using namespace std;

int main()
{
    // int num = 10;
    // int& n = num;
    // n = 1; //关联，num和n的值现在都是1了。
    // cout << num << '\t' << n << endl;

    // const double& ref = 100;
    // cout << ref << endl;

    // // int num = 100;
    // // int& ref_num = num;
    // // ref_num = 118;
    // // // cout << num << '\t' << ref_num << endl;
    // // cout << &num << '\t' << &ref_num << endl;
    // //实际上，在编译器内部是这样的
    // int num = 108;
    // int* ref_num = &num;
    // *ref_num = 118;
    // cout << &num << '\t' << ref_num << endl;

    double score[] {98, 87, 65, 43, 76};
    double* ptr_score;
    ptr_score = &score[0];
    // ptr_score = score;
    // cout << ptr_score << endl;
    // cout << ptr_score[0] << endl;//这两处不用写*很奇怪
    // cout << ptr_score[3] << endl;//这两处不用写*很奇怪
    cout << sizeof(score) << '\t' << sizeof(ptr_score) << endl;
    // double num = 32.00;
    // cout << sizeof(num) << endl;

    return 0;
}