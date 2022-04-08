#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int W, H;
int BRcnt;
bool BR[201][201]; // y, x 좌표에서의 좌->우, 하->상 이 부러진 길인지 여부
long long DP[101] = {1}; // width
int main() {
  cin >> W >> H >> BRcnt;
  int x1, y1, x2, y2;
  for (int i = 1; i <= BRcnt; i++) {
    cin >> x1 >> y1 >> x2 >> y2;
    BR[y1 + y2][x1 + x2] = true;
  }

  for (int Hi = 0; Hi <= H; Hi++) {
    for (int Wi = 0; Wi <= W; Wi++) {
      if (Wi == 0 && Hi == 0) {
        continue;
      }
      if (Hi == 0 || BR[Hi * 2 - 1][Wi * 2]) {
        DP[Wi] = 0; // 아래에서 위로 못갈 때
      }
      if (Wi != 0 && !BR[Hi * 2][Wi * 2 - 1]) {
        DP[Wi] += DP[Wi - 1]; // 좌에서 우로 갈 수 있을 때
      }
    }
  }
  cout << DP[W];
}
