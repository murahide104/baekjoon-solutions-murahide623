#include <iostream>
using namespace std;

long fun(long a, long b);

int main() {
    long a, b;
    cin >> a >> b;
    cout << fun(a,b) << endl;

    return 0;
}

long fun (long a, long b) {
    long result = (a+b)*(a-b);

    return result;
}