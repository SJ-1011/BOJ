#include <iostream>
#include <vector>

using namespace std;

int d(int n) {
    vector<int> q;

    int num = n;

    while(true){
        if (num > 0) {
            q.push_back(num % 10);
            num = int(num / 10);
        }
        else {
            break;
        }
    }

    int sum = 0;

    for (int i = 0; i < q.size(); i++) {
        sum += q[i];
    }
    sum += n;

    return sum;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 생성자 없거나 검사 안함 false
    // 생성자 있음 true
    vector<bool> v(10001);

    for (int i = 1; i <= 10000; i++) {
        v[d(i)] = true;
    }

    for (int i = 1; i <= 10000; i++) {
        if (v[i] == false) {
            cout << i << '\n';
        }
        // cout << v[i] << '\n';
    }

    return 0;
}
