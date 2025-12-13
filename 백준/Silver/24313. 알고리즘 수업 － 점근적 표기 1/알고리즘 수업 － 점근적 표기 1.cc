#include <iostream>
using namespace std;

int main() {
    long long a1, a0, c, n0;
    cin >> a1 >> a0 >> c >> n0;

    if (c - a1 > 0) {
        long long n_required = (a0 + (c - a1) - 1) / (c - a1);
        if (n_required <= n0) cout << 1;
        else cout << 0;
    } 
    else if (c - a1 == 0) {
        if (a0 <= 0) cout << 1;
        else cout << 0;
    } 
    else {
        cout << 0;
    }

    return 0;
}
