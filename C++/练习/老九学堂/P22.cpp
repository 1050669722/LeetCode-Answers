#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

using namespace std;

int main()
{
    // cout << '\a' << endl;

    // string str = "Hello";
    // cout << str << endl;

    double num1 = 272;
    double num2 = 250;
    double num3 = 240;

    cout << left;
    // cout << right;
    cout << setfill('_'); //如果不设置填充，则默认用空格来填充。
    cout << setw(8) << num1 <<
            setw(8) << num2 <<
            setw(8) << num3 << endl;

    return 0;
}