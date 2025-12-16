#include <iostream>

using namespace std;

long long int gcd(long long int a, long long int b){
    long long int mob = b % a;
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

    long long int a, b;

    cin >> a >> b;

    if (a > b) {
        swap(a, b);
    }

    long long int res = gcd(a, b);

    cout << (a * b) / res << endl;

    
    return 0;
}

