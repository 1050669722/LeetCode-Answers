#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

using namespace std;

int main()
{
    int num1 = 5, num2 = 2;
    num1 = num2++ - --num2; //自增、自减的自身性质，以及运算符优先级
    cout << num1 << '\t' << num2 << endl;
    return 0;
}