#include <iostream>
using namespace std;

int main () {
    int a, b;
    cin >> a >> b;
    if(0 < a && 0 < b)
        cout << 1 << endl;
    else if(a < 0 && 0 < b)
        cout << 2 << endl;
    else if(a < 0 && b < 0)
        cout << 3 << endl;
    else
        cout << 4 << endl;

    return 0;
}