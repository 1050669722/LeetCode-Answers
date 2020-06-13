#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    cout << sizeof(double) << endl;
    cout << sizeof(long double) << endl;
    cout << sizeof(3.14) << endl;
    cout << sizeof(3.14f) << endl;

    float numFloat = 10 / 3.0;
    double numDouble = 10 / 3.0;
    cout << fixed;
    cout << setprecision(2);
    cout << "numFloat = " << numFloat * 100000000 << endl;
    cout << "numDouble = " << numDouble * 100000000 << endl;

    cout << "结果" << numDouble * 100000000 << endl;

    system("pause");
    
    return 0;
}