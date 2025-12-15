#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> v(3);
    while (true) {
        cin >> v[0] >> v[1] >> v[2];

        if (v[0] == 0 && v[1] == 0 && v[2] == 0) {
            break;
        }
        sort(v.begin(), v.end());

        if (v[2] >= v[0] + v[1]) {
            cout << "Invalid" << endl;
        } else if (v[0] == v[1] && v[1] == v[2]){
            cout << "Equilateral" << endl;
        } else if (v[0] == v[1] || v[0] == v[2] || v[1] == v[2]) {
            cout << "Isosceles" << endl;
        } else {
            cout << "Scalene" << endl;
        }
    }

    return 0;
}
