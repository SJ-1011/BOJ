#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    long long N;
    cin >> N;
    vector<int> nums;
    while (N > 0){
        nums.push_back(N % 10);
        N /= 10;
    }
    sort(nums.begin(), nums.end(), greater<int>());

    for (int i = 0; i < size(nums); i++){
        cout << nums[i];
    }

    return 0;
}
