#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int N, M;
int parent[1123456];
int cmd[112345][3];

int findRoot(int node) {
  if (parent[node] == node) {
    return node;
  } else {
    parent[node] = findRoot(parent[node]);
    return parent[node];
  }
}

void unite(int a, int b) {
  int aRoot = findRoot(a);
  int bRoot = findRoot(b);

  if (aRoot != bRoot) {
    parent[aRoot] = bRoot;
  }
}

void isUnion(int a, int b) {
  if (findRoot(a) == findRoot(b)) {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
}

int main() {
  cin >> N >> M;
  for (int i = 0; i <= N; i++) {
    parent[i] = i;
  }
  int tmp1, tmp2, tmp3;
  for (int i = 0; i < M; i++) {
    cin >> cmd[i][0] >> cmd[i][1] >> cmd[i][2];
  }

  for (int i = 0; i < M; i++) {
    if (cmd[i][0] == 0) {
      unite(cmd[i][1], cmd[i][2]);
    } else if (cmd[i][0] == 1) {
      isUnion(cmd[i][1], cmd[i][2]);
    }
  }
}
