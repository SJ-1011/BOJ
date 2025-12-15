#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long x, y;
    cin >> n;

    vector<pair<long long, long long>> v(n);

    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        v[i].first = x;
        v[i].second = y;
    }

    long long x_max = -10001;
    long long y_max = -10001;
    long long x_min = 10001;
    long long y_min = 10001;

    for (int i = 0; i < n; i++) {
        x_max = max(x_max, v[i].first);
        y_max = max(y_max, v[i].second);
        x_min = min(x_min, v[i].first);
        y_min = min(y_min, v[i].second);
    }

    long long res;
    res = (x_max - x_min) * (y_max - y_min);

    cout << res;

    return 0;
}
