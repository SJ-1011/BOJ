#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    getline(cin, s);

    string tmp = "";
    vector<string> vs;

    bool flag;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '<') {
            vs.push_back(tmp);
            tmp = "";
            flag = true;
            tmp += s[i];
        } else if (s[i] == '>') {
            flag = false;
            tmp += s[i];
            vs.push_back(tmp);
            tmp = "";
        }
        else if (s[i] == ' ' && !flag) {
            vs.push_back(tmp);
            vs.push_back(" ");
            tmp = "";
        } else {
            tmp += s[i];
        }
    }

    if (tmp != "" || tmp != " ") vs.push_back(tmp);

    for (int i = 0; i < vs.size(); i++) {
        if (vs[i][0] != '<') {
            reverse(vs[i].begin(), vs[i].end());
        }

        cout << vs[i];
    }

    



    return 0;
}
