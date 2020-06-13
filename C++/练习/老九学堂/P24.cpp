#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

using namespace std;

int main()
{
    int num1 = 5, num2 = 2;
    double num3 = num1 / num2; //先除法，然后发生了自动类型转换。 num3得到的就是2
    double num4 = (double)num1 / num2; //num4得到的就是2.5
    cout << num3 << '\t' << num4 << endl; //C中显示2.0

    return 0;
}