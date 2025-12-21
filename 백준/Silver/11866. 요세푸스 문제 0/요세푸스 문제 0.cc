#include <iostream>
#include <algorithm>
#include <numeric>
#include <deque>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n >> k;

    std::deque<int> dq(n);
    std::iota(dq.begin(), dq.end(), 1);
    int p = 0;
    std:: deque<int> ans;

    while (!dq.empty()) {
        p = (p + k - 1) % dq.size();
        ans.push_back(dq[p]);
        dq.erase(dq.begin() + p);
    }

    std::cout << "<";
    for (int i = 0; i < ans.size(); i++) {
        if (i != ans.size() - 1)
            std::cout << ans[i] << ", ";
        else 
            std::cout << ans[i];
    }
    std::cout << ">";

    return 0;
}
