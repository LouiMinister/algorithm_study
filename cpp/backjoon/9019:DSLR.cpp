#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <vector>

using namespace std;

int T;
int inA, inB;
queue<int> q;
bool visited[10001];
pair<int, char> prev[10001];
vector<string> res;

int D(int n) {
  n *= 2;
  if (n > 9999)
    n %= 10000;
  return n;
}
int S(int n) {
  n -= 1;
  if (n == -1)
    n = 9999;
  return n;
}
int L(int n) {
  int left1 = n / 1000;
  n = n - left1 * 1000;
  n = n * 10 + left1;
  return n;
}
int R(int n) {
  int right1 = n % 10;
  n = n - right1;
  n = n / 10 + right1 * 1000;
  return n;
}

void bfs() {
  q.push(inA, ""); // {n ,cmd}
  visited[inA] = true;
  prev[inA] = {inA, ''};

  while (!q.empty()) {
    int nowN = q.front();
    q.pop();
    if (nowN == inB) {
      return;
    }
    int nextN;

    nextN = D(nowN);
    if (!visited[nextN]) {
      q.push(nextN);
      visited[nextN] = true;
      prev[nextN] = {nowN, 'D'};
    }

    nextN = S(nowN);
    if (!visited[nextN]) {
      q.push(nextN);
      visited[nextN] = true;
      prev[nextN] = {nowN, 'S'};
    }

    nextN = L(nowN);
    if (!visited[nextN]) {
      q.push(nextN);
      visited[nextN] = true;
      prev[nextN] = {nowN, 'L'};
    }

    nextN = R(nowN);
    if (!visited[nextN]) {
      q.push(nextN);
      visited[nextN] = true;
      prev[nextN] = {nowN, 'R'};
    }
  }
}

int main() {
  cin >> T;
  for (int TC = 1; TC <= T; TC++) {
    cin >> inA >> inB;
    bfs();
    fill_n(visited, 10001, false);
    fill_n(prev, 10001, pair<int, char>);
    while (!q.empty()) {
      q.pop();
    }
  }
  for (string s : res) {
    cout << s << '\n';
  }
}
