#include <algorithm>
#include <bitset>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

/*
  메모리제한 128MB = 128 * 1024 * 1024 * 8 bit = 1073741824 = 10억비트
  arrow 크기 = 3 * 17000 * 17000 = 289000000 * 3 = 9억비트.. 아 아 근데 잇자나
  copy인 경우면 무적권 글로 가는게 이득아닌가..? 사실 copy인 경우면 다른
  방향으로 갈일이 없네 독립시행이네 그러면 copy 인경우는 bitset을 111로
  해야겠다. 아 근데 이러면.. 세방향으로 가는거랑 겹치는데. 겹치는지 함 확인해봄
  없네 왜냐하면 add 하고 delete는 같이 있을 수가 없네 ㅋㅋ
  그럼 bitset을 111로가자
*/

using namespace std;
const int maxN = 17000;

// bitset<3> arrow[maxN + 1][maxN + 1]; // 00대각 m /  10 위 d / 11 대각 c / 01
// 좌 a
unsigned char arrow[maxN / 2 + 2][maxN / 2 + 2] = {};
int cnt[2][maxN + 1] = {};
string before;
string after;

int getArrow(int ai, int bi) {
  int shifter = 0; // ai ==0 , bi==0
  if (ai % 2 == 1 && bi % 2 == 0) {
    shifter = 2;
  } else if (ai % 2 == 0 && bi % 2 == 1) {
    shifter = 4;
  } else { // ai==1, bi==1
    shifter = 6;
  }
  return (arrow[bi / 2][ai / 2] >> shifter) & 0b11;
}

void setArrow(int ai, int bi, int val) {
  int shifter = 0; // ai ==0 , bi==0
  if (ai % 2 == 1 && bi % 2 == 0) {
    shifter = 2;
  } else if (ai % 2 == 0 && bi % 2 == 1) {
    shifter = 4;
  } else { // ai==1, bi==1
    shifter = 6;
  }
  arrow[bi / 2][ai / 2] = arrow[bi / 2][ai / 2] | (val << shifter);
}

void printAns(int ai, int bi) {
  if (ai <= 0 && bi <= 0) {
    return;
  }
  if (getArrow(ai, bi) == 0b11) { // copy after[ai]
    printAns(ai - 1, bi - 1);
    cout << 'c' << ' ' << after[ai] << endl;
  } else if (getArrow(ai, bi) == 0b01) { // add after[ai]
    printAns(ai - 1, bi);
    cout << 'a' << ' ' << after[ai] << endl;
  } else if (getArrow(ai, bi) == 0b10) { // delete before[bi]
    printAns(ai, bi - 1);
    cout << 'd' << ' ' << before[bi] << endl;
  } else if (getArrow(ai, bi) == 0b00) { // or modify after[ai]
    printAns(ai - 1, bi - 1);
    cout << 'm' << ' ' << after[ai] << endl;
  }
}

int main() {
  cin >> before;
  before = ' ' + before;
  cin >> after;
  after = ' ' + after;

  cnt[0][0] = 0;
  for (int ai = 1; ai <= maxN; ai++) {
    cnt[0][ai] = ai;
    setArrow(ai, 0, 0b01);
    // arrow[0][ai].set(0, 1);
  }

  for (int bi = 1; bi <= before.length() - 1; bi++) { // 세로 증가
    cnt[bi % 2][0] = cnt[(bi + 1) % 2][0] + 1;
    setArrow(0, bi, 0b10);
    // arrow[bi][0].set(2, 1);

    for (int ai = 1; ai <= after.length() - 1; ai++) { // 가로 증가
      if (before[bi] == after[ai]) { // a의 ai번째 문자랑 b의 bi번째 문자가
        cnt[bi % 2][ai] = cnt[(bi + 1) % 2][ai - 1];
        setArrow(ai, bi, 0b11);
        // arrow[bi][ai].set();
      } else {
        int case1 = cnt[(bi + 1) % 2][ai] + 1;
        int case2 = cnt[(bi + 1) % 2][ai - 1] + 1;
        int case3 = cnt[bi % 2][ai - 1] + 1;
        int minCase = min({case1, case2, case3});
        cnt[bi % 2][ai] = minCase;
        if (minCase == case1) { // delete after[ai]
          setArrow(ai, bi, 0b10);
          // arrow[bi][ai].set(2, 1);
        } else if (minCase == case2) { // modify to after[ai]
          setArrow(ai, bi, 0b00);
          // arrow[bi][ai].set(1, 1);
        } else if (minCase == case3) { // add before[bi]
          setArrow(ai, bi, 0b01);
          // arrow[bi][ai].set(0, 1);
        }
      }
      // test start
      cout << cnt[bi % 2][ai] << ' ';
    }
    cout << endl;
    // test-end
  }

  // test start
  for (int bi = 0; bi <= before.length() - 1; bi++) {
    for (int ai = 0; ai <= after.length() - 1; ai++) {
      cout << getArrow(ai, bi) << ' ';
    }
    cout << endl;
  }
  // test end

  printAns(after.length() - 1, before.length() - 1);
}
