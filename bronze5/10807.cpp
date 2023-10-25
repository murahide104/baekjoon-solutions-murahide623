#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> vec(n);
    for (int i = 0; i < n; i++)
        cin >> vec.at(i);
    
    int v;
    cin >> v;

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (vec.at(i) == v)
            cnt++;
    }

    cout << cnt << endl;
}