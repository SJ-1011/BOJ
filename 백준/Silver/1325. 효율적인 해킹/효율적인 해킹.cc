#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int bfs(int start, const vector<vector<int>>& graph, int n) {
    vector<bool> visited(n + 1, false);
    queue<int> q;
    q.push(start);
    visited[start] = true;
    int count = 1;

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int next : graph[node]) {
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
                count++;
            }
        }
    }

    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1);

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        graph[b].push_back(a);  // b를 해킹하면 a도 해킹됨
    }

    int max_result = 0;
    vector<int> result;

    for (int i = 1; i <= n; ++i) {
        int temp = bfs(i, graph, n);
        if (temp > max_result) {
            max_result = temp;
            result.clear();
            result.push_back(i);
        } else if (temp == max_result) {
            result.push_back(i);
        }
    }

    for (int i : result) {
        cout << i << ' ';
    }

    return 0;
}
