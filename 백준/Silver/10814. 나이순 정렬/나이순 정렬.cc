#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

struct ageList
{
    int age;
    int num;
    string name;
};


bool cmp(const ageList &a, const ageList &b) {
    if (a.age != b.age) {
        return a.age < b.age;
    }
    return a.num < b.num;
}

int main() {
    int n;
    cin >> n;
    vector<ageList> v(n);
    for (int i = 0; i < n; i++) {
        cin >> v[i].age >> v[i].name;
        v[i].num = i;
    }

    sort(v.begin(), v.end(), cmp);
    for (int i = 0; i < n; i++) {
        cout << v[i].age << ' ' << v[i].name << endl;
    }

    return 0;
}
