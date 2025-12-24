#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;

int mode(const vector<int>& v) {
    map<int, int> cnt;

    for (int x : v) {
        cnt[x]++;
    }

    int maxFreq = 0;
    for (auto& [value, freq] : cnt) {
        if (freq > maxFreq) {
            maxFreq = freq;
        }
    }

    vector<int> candidates;
    for (auto& [value, freq] : cnt) {
        if (freq == maxFreq) {
            candidates.push_back(value);
        }
    }

    // 최빈값이 여러 개면 두 번째로 작은 값
    if (candidates.size() > 1) {
        return candidates[1];
    } else {
        return candidates[0];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int k;
    int sum = 0;
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        cin >> k;
        v[i] = k;
        sum += k;
    }

    sort(v.begin(), v.end());
    double avg = double(sum) / double(n);
    cout << (long long)round(avg) << '\n';
    cout << v[n/2] << '\n';

    int choibin = mode(v);
    cout << choibin << '\n';

    cout << v[n-1] - v[0] << '\n';

    




    return 0;
}
