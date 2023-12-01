#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    string s;

    for (int i=0; i < n; i++) {
        cin >> s;
        cout << s.at(0) << s.at(s.size() - 1) << endl;
    }
}