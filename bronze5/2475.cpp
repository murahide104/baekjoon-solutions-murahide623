#include <iostream>
using namespace std;

int square(int x);

int main() {
    int array[5];
    int i;
    for(i = 0; i < 5; i++){
        cin >> array[i];
    }
    int result = 0;
    for(i = 0; i < 5; i++){
        result += square(array[i]);
    }
    cout << result % 10 << endl;

    return 0;
}

int square (int x) {
    int result = x * x;

    return result;
}