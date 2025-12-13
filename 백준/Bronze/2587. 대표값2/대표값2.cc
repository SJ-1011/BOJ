#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c, d, e;
    cin >> a >> b >> c >> d >> e;
    double avg = (a+b+c+d+e) / 5.0;
    int arr[] = {a, b, c, d, e};
    sort(arr, arr + 5);

    cout << avg << endl << arr[2];

    return 0;
}
