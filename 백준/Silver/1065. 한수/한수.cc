#include <iostream>
#include <string>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int sum = 0;

    for (int i = 1; i <= n; i++){
        if (i < 100) {
            sum += 1;
        } else {
            string s = to_string(i);
            bool flag = true;
            for (int j = 0; j < s.size() - 2; j++) {
                if (s[j+1] - s[j] != s[j+2] - s[j+1]) {
                    flag = false;
                    break;
                }
            }
            if (flag) sum += 1;
        }
        
    }

    cout << sum;
    return 0;
}
