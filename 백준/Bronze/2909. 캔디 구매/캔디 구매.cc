#include <iostream>
#include <math.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int c, k;
    cin >> c >> k;

    
    int num = 5 * pow(10, k-1);

    int res = int((c + num) / pow(10, k)) * pow(10, k);
    
    cout << res;
    return 0;
}
