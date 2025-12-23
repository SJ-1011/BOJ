#include <iostream>
#include <chrono>
#include <ctime>

int main() {
    using namespace std;

    auto now = chrono::system_clock::now();

    time_t now_time = chrono::system_clock::to_time_t(now);

    now_time += 9 * 60 * 60;

    tm* seoul = gmtime(&now_time);

    cout << (seoul->tm_year + 1900) << "-"
         << (seoul->tm_mon + 1) << "-"
         << seoul->tm_mday << "\n";
}
