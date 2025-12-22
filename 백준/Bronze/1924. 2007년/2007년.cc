#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int month, date;
    cin >> month >> date;

    int ans = 0;

    ans += date;

    for (int i = 0; i < month; i++) {
        switch (i)
        {
        case 0:
            break;
            
        case 1:
            ans += 31;
            break;
            
        case 2:
            ans += 28;
            break;
            
        case 3:
            ans += 31;
            break;
            
        case 4:
            ans += 30;
            break;
            
        case 5:
            ans += 31;
            break;
            
        case 6:
            ans += 30;
            break;
            
        case 7:
            ans += 31;
            break;
            
        case 8:
            ans += 31;
            break;
            
        case 9:
            ans += 30;
            break;
            
        case 10:
            ans += 31;
            break;
            
        case 11:
            ans += 30;
            break;
        
        default:
            break;
        }
    }

    ans = ans % 7;
    switch (ans)
    {
    case 1:
        cout << "MON";
        break;
    case 2:
        cout << "TUE";
        break;
    case 3:
        cout << "WED";
        break;
    case 4:
        cout << "THU";
        break;
    case 5:
        cout << "FRI";
        break;
    case 6:
        cout << "SAT";
        break;
    
    default:
        cout << "SUN";
        break;
    }

    return 0;
}
