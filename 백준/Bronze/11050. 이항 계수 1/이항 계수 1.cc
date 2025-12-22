#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;

    long long ans = 1;
    int m = n;

    for (int i = 0; i < k; i++){
        ans *= m;
        m -= 1;
    }

    for (int i = 1; i <= k; i++) {
        ans /= i;
    }

    cout << ans;

    return 0;
}
