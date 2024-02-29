#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const int MOD = 1e9 + 7;
const ll INF = 1e18;


//Write brute force solution here
void solve() {
    int n;
    cin >> n;
    if (n > 20) {
        cout << -1 << endl;
    } else {
        cout << n << endl;
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
//    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}