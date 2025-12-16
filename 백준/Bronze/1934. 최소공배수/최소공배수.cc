#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b){
    long long mob = b % a;
    while (mob != 0) {
        b = a;
        a = mob;
        mob = b % a;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    vector<long long> v(2);

    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> v[0] >> v[1];
        sort(v.begin(), v.end());
        long long res = gcd(v[0], v[1]);

        cout << (v[0] * v[1]) / res << endl;

    }
    
    return 0;
}

