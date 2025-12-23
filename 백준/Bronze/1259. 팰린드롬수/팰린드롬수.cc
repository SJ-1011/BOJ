#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        string num;
        cin >> num;
        
        if (num == "0") {
            break;
        }

        bool flag = true;
        for (int i = 0; i < num.size() / 2; i++) {
            if (num[i] != num[num.size() - 1 - i]){
                flag = false;
                break;
            }
        }

        if (flag)
            cout << "yes" << '\n';
        else
            cout << "no" << '\n';

    }

    return 0;
}
