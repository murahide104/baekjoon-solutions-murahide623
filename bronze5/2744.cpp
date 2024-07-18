#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string t;
    cin >> t;

    for (int i=0; i < t.size(); i++) {
        if (isupper(t.at(i))) {
            cout << (char)tolower(t.at(i));
        }
        else {
            cout << (char)toupper(t.at(i));
        }
    }

    cout << endl;
