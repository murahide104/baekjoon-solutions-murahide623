#include <bits/stdc++.h>
using namespace std;

float charCheck (char c) {
    if (c == 'A')
        return 4.0;
    else if (c == 'B')
        return 3.0;
    else if (c == 'C')
        return 2.0;
    else if (c == 'D')
        return 1.0;
    else if (c == '+')
        return 0.3;
    else if (c == '0')
        return 0.0;
    else if (c == '-')
        return -0.3;
    else
        return 0.0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    cout << fixed << setprecision(1);
    if (s == "F")
        cout << 0.0 << endl;
    else
        cout << charCheck(s.at(0)) + charCheck(s.at(1)) << endl;
}