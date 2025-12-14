#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;


int main() {
    long long n, num;
    cin >> n;

    vector<long long> quest;
    vector<long long> sub;
    vector<long long> stack;
    unordered_map<long long, long long> where;

    for (int i = 0; i < n; i++) {
        cin >> num;
        quest.push_back(num);
        sub.push_back(num);
    }

    sort(sub.begin(), sub.end());

    for (int i = 0; i < n; i++) {
        if (i == 0 || sub[i] != sub[i - 1]) {
            where[sub[i]] = where.size();
        }
    }

    for (int i = 0; i < size(quest); i++) {
        // quest[i]가 stack의 몇 번째에 있는지 알아내야함
        cout << where[quest[i]] << ' ';
    }



    return 0;
}
