#include <iostream>
using namespace std;

int main() {
    int a, b, c, d, e, f, x, y;
    cin >> a >> b >> c >> d >> e >> f;
    bool found = false;
    for (int i = -999; i <= 999 && !found; i++) {
        for (int j = -999; j <= 999; j++) {
            if (a*i + b*j == c && d*i + e*j == f) {
                x = i;
                y = j;
                found = true;
                break;
            }
        }
    }

    cout << x << ' ' << y;

    return 0;
}
