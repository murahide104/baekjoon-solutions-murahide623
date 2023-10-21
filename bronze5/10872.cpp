#include <iostream>
using namespace std;

int main() {
    int n, total;
    cin >> n;
    total = 1;

    for (; 0 < n; n--) {
        total *= n;
    }

    cout << total << endl;

    return 0;
}