#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    
    int total = 0;
    for (int i=1; i <= n; i++) {
        total += i;
    }

    cout << total << endl;
}