#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int month, date;
    cin >> month >> date;

    int daysInMonth[] = {
        31, 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    };

    string dayOfWeek[] = {
        "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"
    };

    int total = date;

    for (int i = 0; i < month - 1; i++) {
        total += daysInMonth[i];
    }

    cout << dayOfWeek[total % 7] << '\n';

    return 0;
}
