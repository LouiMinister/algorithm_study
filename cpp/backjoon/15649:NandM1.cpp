#include <algorithm>
#include <iostream>
const int MAX = 9;

using namespace std;

int cnt = 0;
int N, M;
int cur[MAX] = {
    0,
};
bool visited[MAX] = {
    0,
};

void checkValue(int cnt) {
  if (cnt == M) {
    for (int i = 1; i <= M; i++) {
      cout << cur[i] << ' ';
    }
    cout << '\n';
    return;
  }
  for (int i = 1; i <= N; i++) {
    if (visited[i] == false) {
      visited[i] = true;
      cur[cnt + 1] = i;
      checkValue(cnt + 1);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> N >> M;
  checkValue(0);
}
