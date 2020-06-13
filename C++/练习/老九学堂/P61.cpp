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
    // double score[] {98, 87, 65, 43, 76};
    // double* ptr_score = &score[0];
    // for (int i = 0; i < 5; ++i)
    // {
    //     cout << *ptr_score++ << endl;
    // }

    int i;
    double score[] {98, 87, 65, 43, 76};
    double* ptr_score = &score[1]; //score + 1;//
    ptr_score += 2;
    cout << *ptr_score << endl;
    ptr_score -= 3;
    cout << *ptr_score << endl;

    return 0;
}