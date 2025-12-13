#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int x, y, w, h;
    cin >> x >> y >> w >> h;
    int ans = min({x, y, w-x, h-y});
    cout << ans;
    return 0;
}