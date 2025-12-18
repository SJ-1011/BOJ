#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(long long n){
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (long long i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    long long n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n;
        if (n <= 2) {
            cout << 2 << '\n';
            continue;
        }
        if (n % 2 == 0) n++;

        while (true){
            if (isPrime(n)) {
                cout << n << '\n';
                break;
            }
            n += 2;
        }
    }

    return 0;
}
