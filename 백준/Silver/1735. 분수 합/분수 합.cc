#include <iostream>

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

    long long a, b, c, d;

    cin >> a >> b;
    cin >> c >> d;

    long long up, down;
    down = b * d;
    long long down2 = down;
    up = a*d + c*b;
    long long up2 = up;

    if (up > down) {
        swap(up, down);
    }

    long long res = gcd(up, down);

    cout << up2 / res << ' ' << down2 / res << endl;

    
    return 0;
}

