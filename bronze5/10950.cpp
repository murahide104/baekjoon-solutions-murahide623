#include <iostream>
using namespace std;

int main() {
    int t, a, b;
    cin >> t;

    int i;
    for (i=0; i < t; i++) {
        cin >> a  >> b;
        cout << a+b << endl;
    }

    return 0;
}