#include <iostream>
#include <vector>

using namespace std;


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    int H, W, N;
    for (int i = 0; i < T; i++) {
        cin >> H >> W >> N;
        vector<int> v = {0, 1};
        for (int j = 1; j <= N; j++){
            // j번째 사람한테 배정될 방
            v[0]++;

            // H를 넘어서는지 검사
            if (v[0] > H) {
                v[0] = 1;
                v[1]++;
            }

        }

        if (v[1] < 10)
            cout << v[0] << '0' << v[1] << '\n';
        else
            cout << v[0] << v[1] << '\n';

    }
    
    return 0;
}
