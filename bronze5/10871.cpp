#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    int result;
    for (int i = 0; i < n; i++) {
        cin >> result;
        if (result < x)
            cout << result << " ";
    }
    
    cout << endl;

    return 0;
}