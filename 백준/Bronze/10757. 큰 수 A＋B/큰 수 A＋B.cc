#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    cin >> a >> b;

    // 길이 맞추기
    if (a.size() < b.size()) {
        a.insert(0, b.size() - a.size(), '0');
    } else if (b.size() < a.size()) {
        b.insert(0, a.size() - b.size(), '0');
    }

    string ans = "";
    int carry = 0;

    // 뒤에서부터 덧셈
    for (int i = a.size() - 1; i >= 0; i--) {
        int sum = (a[i] - '0') + (b[i] - '0') + carry;
        carry = sum / 10;
        ans = char(sum % 10 + '0') + ans;
    }

    // 마지막 올림 처리
    if (carry) {
        ans = '1' + ans;
    }

    cout << ans;
    return 0;
}
