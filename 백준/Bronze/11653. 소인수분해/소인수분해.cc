#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isPrime(int);
int main() {
    int N;
    cin >> N;
    vector<int> nums;
    if (N == 1){
        return 0;
    }

    int sample = N;
    while (true){
        for (int i = 2; i <= sqrt(sample); i++){
            if (sample % i == 0){
                nums.push_back(i);
                sample = sample / i;
                break;
            }
        }
        if (isPrime(sample)){
            nums.push_back(sample);
            break;
        }
    }

    for (int x : nums) {
        cout << x << endl;
    }
    return 0;
}

bool isPrime(int num){
    if (num == 2 || num == 1){
        return true;
    }
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0){
            return false;
        }
    }
    return true;
}