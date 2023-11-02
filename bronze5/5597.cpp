#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> vec(28);

    for (int i = 0; i < 28; i++)
        cin >> vec.at(i);

    for (int i = 1; i <= 30; i++) {
        if (find(vec.begin(), vec.end(), i) == vec.end())
            cout << i << endl;
    }
}