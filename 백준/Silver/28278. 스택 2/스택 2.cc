#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, command, x;
    cin >> n;

    vector<int> v;

    for (int i = 0; i < n; i++){
        cin >> command;

        switch (command) {
            case 1:
                cin >> x;
                v.push_back(x);
                break;
            case 2:
                if (v.size() > 0) {
                    int res = v.back();
                    v.pop_back();
                    cout << res << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
            case 3:
                cout << v.size() << '\n';
                break;
            case 4:
                if (v.size() == 0) {
                    cout << 1 << '\n';
                } else {
                    cout << 0 << '\n';
                }
                break;
            case 5:
                if (v.size() > 0) {
                    int res = v.back();
                    cout << res << '\n';
                } else {
                    cout << -1 << '\n';
                }
                break;
        }
    }
    
    return 0;
}

