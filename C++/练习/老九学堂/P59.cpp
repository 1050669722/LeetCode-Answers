#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

int main()
{
    // double* ptr_double = NULL;//nullptr;//0;//
    // cout << ptr_double << endl;

    double objNum = 3.14;
    double* ptr_obj = &objNum;
    void* vptr_obj = &objNum;
    cout << boolalpha;
    cout << (ptr_obj == vptr_obj) << endl;
    *ptr_obj = 10;
    cout << objNum << endl;
    // *vptr_obj = 20;
    // cout << objNum << endl;
    double* ptr = ptr_obj;
    cout << ptr << endl;
    // double* ptr = vptr_obj;
    // cout << ptr << endl;

    return 0;
}