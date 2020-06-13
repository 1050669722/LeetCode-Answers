#include <iostream>

using namespace std;

// 分配基础数据类型
void func1()
{
    // malloc 和 free
    // 分配空间
    int *p1 = (int *)malloc(sizeof(int)/sizeof(char));
    // 释放空间
    free(p1);

    // new 和 delete
    // 分配空间：new type
    int *p2 = new int;
    *p2 = 10;
    cout << *p2 << endl;
    //释放空间：delete pointer
    delete p2;

    // new 在分配单个变量空间的时候，可以对空间进行初始化
    int *p3 = new int(10);
    cout << *p3 << endl;

}

// 分配数组
void func2()
{
    // malloc 和 free
    int *p1 = (int *)malloc(sizeof(int)/sizeof(char)*10); //p1指向这一空间
    free(p1);

    // new 和 delete
    // new type[数量]
    // new在分配数组空间的同时，不能进行初始化
    int *p2 = new int[10]; //int a[10]
    for (int i = 0; i < 10; ++i)
    {
        p2[i] = i; //单个变量就要用*取值运算符，但是数组就不用这个符号了。 //此时就是p2首地址 //如果a是数组，a和&a
    }
    for (int i = 0; i < 10; ++i)
    {
        cout << p2[i] << ' ';
    }
    cout << endl;
    // delete[] 指针 //如果不加[]，实际上只释放一个对象
    // 一定要加上[]，否则会造成内存泄漏 //内存泄漏指的是由于疏忽或错误造成了程序未能释放掉不再使用的内存。性能不良，内存会耗尽。
    /**
     * C++没有垃圾回收机制，我们需要关注那些类型的内存泄漏？
     * 堆内存泄漏。在内存中程序员手动分配的一块内存，malloc\realloc\new。完成相关操作后，没有调用相对应的free\delete释放掉内存，这时这块内存就会常驻内存，造成堆内存泄漏
    系统资源泄漏。分配给程序使用的资源没有使用相应函数释放，如bitmap\handle\socket.
     */
    delete[] p2;

    //接下来的问题是在堆上进行二维数组的分配

}

int main()
{
    // func1();
    func2();

    return 0;
}