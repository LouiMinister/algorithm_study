#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <vector>

using namespace std;

int N, M;
vector<pair<int, int>> car; // {x,y}
vector<pair<int, int>> pk;  // {x,y}
int dist[123][123];
char area[51][51];
vector<int> graph[123];
bool visited[123];
int partner[123];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void setDist(int carIdx) {
  int visited[51][51];
  fill_n(&visited[0][0], 51 * 51, -1);
  queue<pair<int, int>> q;
  visited[car[carIdx].second][car[carIdx].first] = 0;
  q.push({car[carIdx].first, car[carIdx].second});
  while (!q.empty()) {
    int curX = q.front().first;
    int curY = q.front().second;
    q.pop();
    for (int i = 0; i < 4; i++) {
      int nxtX = curX + dx[i];
      int nxtY = curY + dy[i];
      if (nxtX < 1 || nxtY < 1 || nxtX > M || nxtY > N)
        continue;
      if (area[nxtY][nxtX] == 'X')
        continue;
      if (visited[nxtY][nxtX] != -1)
        continue;
      visited[nxtY][nxtX] = visited[curY][curX] + 1;
      q.push({nxtX, nxtY});
    }
  }
  for (int i = 0; i < pk.size(); i++) {
    dist[carIdx][i] = visited[pk[i].second][pk[i].first];
  }
}

void setGraph(int mid) {
  for (int i = 0; i < car.size(); i++) {
    for (int j = 0; j < pk.size(); j++) {
      if (dist[i][j] != -1 && dist[i][j] <= mid) {
        graph[i].push_back(j);
      }
    }
  }
}

bool dfs(int fromNode) {
  for (int toNode : graph[fromNode]) {
    if (visited[toNode])
      continue;
    visited[toNode] = true;
    if (partner[toNode] == -1 || dfs(partner[toNode])) {
      partner[toNode] = fromNode;
      return true;
    }
  }
  return false;
}

bool check(int mid) {
  for (int i = 0; i < 123; i++) {
    graph[i].clear();
  }
  setGraph(mid);
  int cnt = 0;
  fill_n(partner, 123, -1);
  for (int i = 0; i < car.size(); i++) {
    fill_n(visited, 123, false);
    cnt += dfs(i);
  }
  return cnt == car.size();
}

int binarySearch() {
  int res = -1;
  int lhs = 0;
  int rhs = 12345;
  while (lhs <= rhs) {
    int mid = (lhs + rhs) / 2;
    if (check(mid)) {
      res = mid;
      rhs = mid - 1;
    } else {
      lhs = mid + 1;
    }
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cin >> N >> M;
  string in;
  for (int i = 1; i <= N; i++) {
    cin >> in;
    for (int j = 1; j <= M; j++) {
      area[i][j] = in[j - 1];
      if (area[i][j] == 'C')
        car.push_back({j, i});
      if (area[i][j] == 'P')
        pk.push_back({j, i});
    }
  }
  if (car.size() > pk.size()) {
    cout << -1;
    return 0;
  }
  if (car.size() == 0) {
    cout << 0;
    return 0;
  }

  for (int i = 0; i < car.size(); i++) {
    setDist(i);
    // if (dist[i] == -1) {
    //   cout << -1;
    //   return 0;
    // }
  }

  int res = binarySearch();
  cout << res;
}
