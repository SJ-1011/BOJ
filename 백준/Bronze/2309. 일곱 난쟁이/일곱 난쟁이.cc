#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d, e, f, g, h, i;
    cin >> a >> b >> c >> d >> e >> f >> g >> h >> i;

    vector<int> v = {a, b, c, d, e, f, g, h, i};
    vector<int> select = {0, 0, 1, 1, 1, 1, 1, 1, 1};
    sort(v.begin(), v.end());

    do {
        int sum = 0;
        for (int i = 0; i < v.size(); i++) {
            if (select[i]) sum += v[i];
        }
        if (sum == 100) {
        for (int i = 0; i < v.size(); i++) {
            if (select[i]) cout << v[i] << '\n';
        }
        return 0;
    }
    } while (next_permutation(select.begin(), select.end()));



    return 0;
}
