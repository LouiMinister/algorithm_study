
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <string>
#include <vector>

#define xx first
#define yy second

using namespace std;

int N;
long long dist[123][123];                // �л� -> Ʃ�� �Ÿ�
vector<pair<long long, long long>> stud; // �л��� {x,y}
vector<pair<long long, long long>> tute; // Ʃ���� {x,y}
long long maxDist = 0;
long long minDist = 412312312;
int occBy[123];
bool vis[123]; // -1 �ʱ�ȭ
long long mid;

bool dfs(int from) {
  for (int to = 0; to < N; to++) { // ���� ��ȸ
    if (dist[from][to] > mid)
      continue; // ���� ���� mid������ �л� - Ʃ�� ���� �Ÿ��� ũ�� �ȵ�
    if (vis[to])
      continue;
    vis[to] = true;
    if (occBy[to] == -1 || dfs(occBy[to])) {
      occBy[to] = from;
      return true;
    }
  }
  return false;
}

int bipartite() {
  int cnt = 0;
  fill_n(occBy, 123, -1);
  for (int i = 0; i < N; i++) {
    fill_n(vis, 123, false);
    if (dfs(i)) { //��Ī �����ϸ�
      cnt++;
    }
  }
  return cnt;
}

bool check() {
  return bipartite() == N; // N�� ��Ī �����ϸ� true
}

int main() {
  cin >> N;
  long long in1, in2;
  for (int i = 1; i <= N; i++) {
    cin >> in1 >> in2;
    stud.push_back({in1, in2});
  }
  for (int i = 1; i <= N; i++) {
    cin >> in1 >> in2;
    tute.push_back({in1, in2});
  }

  for (int i = 0; i < N; i++) {   // �л� ��ȸ
    for (int j = 0; j < N; j++) { // Ʃ�� ��ȸ
      dist[i][j] = abs(stud[i].xx - tute[j].xx) + abs(stud[i].yy - tute[j].yy);
      maxDist = max(maxDist, dist[i][j]);
      minDist = min(minDist, dist[i][j]);
    }
  }

  long long l = 0;
  long long r = maxDist;
  long long res = maxDist;
  while (l <= r) {
    mid = (l + r) / 2;
    if (check()) {
      res = min(res, mid);
      r = mid - 1;
    } else {
      l = mid + 1;
    }
  }
  cout << res;
}
