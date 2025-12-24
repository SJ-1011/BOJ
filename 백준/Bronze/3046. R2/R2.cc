#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R1, S;
    cin >> R1 >> S;

    // (r1+b) = s*2

    cout << S*2 - R1;
    
    return 0;
}
