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

class Solution {
public:
    string defangIPaddr(string address) {
        string stack;
        for (int k = 0; k < address.size(); ++k)
        {
            if (address[k] == '.')
            {
                stack.push_back('[');
                stack.push_back('.');
                stack.push_back(']');
            }
            else
            {
                stack.push_back(address[k]);
            }
        }
        return stack;
    }
};

int main()
{
    string address = "255.100.50.0";
    Solution solu;
    string ans = solu.defangIPaddr(address);
    cout << ans << endl;
    return 0;
}