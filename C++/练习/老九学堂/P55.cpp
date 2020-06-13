#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

#include <vector> //vector
#include <ctime>
#include <cstdlib>
#include <algorithm> //sort

using namespace std;

int main()
{
    vector<double> vecDouble = {98.5, 67.9, 43.6, 32.9}; //也可以不写等号
    // vector<double> vecDouble(3);
    // cout << vecDouble.size() << endl; 
    // cout << vecDouble << endl;
    // cout << vecDouble[100] << endl;
    // cout << vecDouble.size() << endl;
    // cout << vecDouble.capacity() << endl;
    // system("pause"); 
    //向容器中插入元素
    vecDouble.push_back(100.8); //在容器的尾部插入一个元素

    // //遍历1
    // for (int i = 0; i<vecDouble.size(); i++)
    // {
    //     cout << vecDouble[i] << endl;
    // }
    // //遍历2 集合的通用遍历方法 使用迭代器 iterator 变量
    vector<double>::iterator it;//这里用到了一个域运算符 声明此迭代器对象来自于哪一个域 某一类型的迭代器 示例化迭代器对象 实际上它是一个类似于指针的对象
    // for (it = vecDouble.begin(); it != vecDouble.end(); ++it) //这里的++是运算符重载了 如果++写在和后面会导致缓存的增加，效率不高 所以迭代器的++写在前面更好
    // {
    //     cout << *it << endl;//*表示对地址取值
    // }

    //排序
    sort(vecDouble.begin(), vecDouble.end());
    for (it = vecDouble.begin(); it != vecDouble.end(); ++it)
    {
        cout << *it << endl;
    }
    // cout << vecDouble[0] << endl;
    // cout << vecDouble.at(1) << endl;

    cout << vecDouble.size() <<endl;

    // cout << vecDouble.empty() << endl;
    // vecDouble.clear();
    // cout << vecDouble.empty() << endl;

    return 0;
}