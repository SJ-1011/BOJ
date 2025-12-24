#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int bfs(vector<vector<int>> v, int n, int m, int x, int y, vector<vector<bool>> &visited){
    deque<pair<int, int>> dq;

    vector<pair<int, int>> direct = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

    visited[y][x] = true;
    dq.push_back({x, y});

    int ans = 1;

    while (dq.size() > 0) {
        int curr_x = dq[0].first;
        int curr_y = dq[0].second;
        dq.erase(dq.begin());
        for (int i = 0; i < 4; i++) {
            int next_x = curr_x + direct[i].first;
            int next_y = curr_y + direct[i].second;

            if (next_x >= 0 && next_y >= 0 && next_x < m && next_y < n) {
                if (v[next_y][next_x] == 0) {
                    if (!visited[next_y][next_x]) {
                        dq.push_back({next_x, next_y});
                        visited[next_y][next_x] = true;
                        ans++;
                    }
                }
            }
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, m;
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m));
    vector<pair<int, int>> empty;
    vector<pair<int, int>> virus;

    int wall = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++){
            cin >> grid[i][j];
            if (grid[i][j] == 0) {
                empty.push_back({j, i});
            } else if (grid[i][j] == 2) {
                virus.push_back({j, i});
            } else if (grid[i][j] == 1) {
                wall += 1;
            }
        }
    }

    int danger = m*n;

    for (int i = 0; i < empty.size(); i++) {
        for (int j = i+1; j < empty.size(); j++) {
            for (int k = j+1; k < empty.size(); k++) {
                grid[empty[i].second][empty[i].first] = 1;
                grid[empty[j].second][empty[j].first] = 1;
                grid[empty[k].second][empty[k].first] = 1;
                int s = 0;
                vector<vector<bool>> visited(n, vector<bool>(m));
                for (int l = 0; l < virus.size(); l++) {
                    s += bfs(grid, n, m, virus[l].first, virus[l].second, visited);
                }
                danger = min(danger, s);
                grid[empty[i].second][empty[i].first] = 0;
                grid[empty[j].second][empty[j].first] = 0;
                grid[empty[k].second][empty[k].first] = 0;
            }
        }
    }
    cout << m * n - (danger + wall + 3);

    return 0;
}
