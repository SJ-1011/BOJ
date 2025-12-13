#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    set<string> s(arr.begin(), arr.end());
    vector<string> v(s.begin(), s.end());
    vector<pair<int, int>> arr2(v.size());

    for (int i = 0; i < v.size(); i++){
        arr2[i].first = v[i].size();
        arr2[i].second = i;
    }
    
    sort(arr2.begin(), arr2.end());
    for (int i = 0; i < arr2.size(); i++) {
        cout << v[arr2[i].second] << endl;
    }
    return 0;
}
