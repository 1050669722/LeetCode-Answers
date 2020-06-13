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
    // double num = 1024.5;
    // double* ptr_num = &num; //可以用下划线表示指向。
    // cout << num << endl;
    // cout << &num << endl;
    // cout << ptr_num << endl;
    // cout << *ptr_num << endl;
    // cout << &ptr_num << endl;

    char ch = 'a';
    char* ptr_ch = &ch; //char*被默认为字符串地址，这与底层有关。
    cout << (void*)ptr_ch << endl; //任意类型的指针 不管什么类型 总之打印出来。  
    cout << *ptr_ch << endl;

    return 0;
}