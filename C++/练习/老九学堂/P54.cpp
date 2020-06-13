#include <iostream>
#include <iomanip>
#include <cmath>
#include <windows.h>

using namespace std;

int main()
{
    string stuNames[] {"a", "b", "c"};
    string courseNames[] {"Chinese", "Math", "English"};
    const int ROW = sizeof(stuNames) / sizeof(stuNames[0]);
    const int COL = sizeof(courseNames) / sizeof(courseNames[0]);

    double scores[ROW][COL];

    for (int i = 0; i<ROW; i++) {
        for (int j = 0; j<COL; j++) {
            cout << "the " << courseNames[j] << " score of " << stuNames[i] << " is: ";
            cin >> scores[i][j];
        }
    }

    cout << '\t';
    for (int i = 0; i < COL; i++) {
        cout << courseNames[i] << '\t';
    }
    cout << endl;
    for (int i = 0; i < ROW; i++) {
        cout << stuNames[i] << '\t';
        for (int j = 0; j < COL; j++) {
            cout << scores[i][j] << '\t';
        }
        cout << endl;
    }

    system("pause");

    return 0;
}