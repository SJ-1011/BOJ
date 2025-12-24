#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    string ans;

    for (int i = 1; i <= s.size(); i++) {
        ans.push_back(s[i-1]);
        if (i % 10 == 0) {
            ans.push_back('\n');
        }
    }

    cout << ans;
    
    return 0;
}
