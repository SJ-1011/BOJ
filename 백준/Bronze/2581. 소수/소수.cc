#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int);

int main() {
    int N, M;
    cin >> N >> M;

    int sum = 0;
    int low = M;
    for (int i = N; i <= M; i++){
        bool res = isPrime(i);
        if (res){
            low = min(low, i);
            sum += i;
        }
    }
    if (sum > 0) {

        cout << sum << endl << low;
    } else {
        cout << -1;
    }
    return 0;
}

bool isPrime(int num){
    if (num == 1) {
        return false;
    }
    else if (num == 2){
        return true;
    }
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0){
            return false;
        }
    }
    return true;
}
