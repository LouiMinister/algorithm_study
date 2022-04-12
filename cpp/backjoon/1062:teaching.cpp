#include <algorithm>
#include <bitset>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N, K;        // 1<=N<=5, 0<=K<=26
int bitWord[51]; // 단어는 50개보다 작거나 같은 개수
int main() {
  int res = 0;
  cin >> N >> K;
  string strary[10];
  for (int i = 1; i <= N; i++) {
    string word;
    cin >> word;
    word = word.substr(4, word.length() - 8);
    for (char c : word) {
      if (c != 'a' && c != 'c' && c != 't' && c != 'i' && c != 'n')
        bitWord[i] |= (1 << (c - 'a'));
    }
  }
  if (K < 5) {
    cout << 0;
    return 0;
  }

  string candidate = "bdefghjklmopqrsuvwxyz";
  bool permut[21];
  for (int i = 0; i < 21; i++) {
    if (i < K - 5) {
      permut[i] = true;
    } else {
      permut[i] = false;
    }
  }
  sort(permut, permut + 21);
  do {
    int bitCandidate = 0;
    for (int i = 0; i < 21; i++) {
      if (permut[i]) {
        bitCandidate |= (1 << (candidate[i] - 'a'));
      }
    }

    int cnt = 0;
    for (int i = 1; i <= N; i++) {
      bitset<26> a = bitset<26>(bitWord[i]);
      bitset<26> b = bitset<26>(bitCandidate);
      if ((bitWord[i] & bitCandidate) == bitWord[i]) {
        cnt++;
      }
    }
    res = max(res, cnt);
  } while (next_permutation(permut, permut + 21));
  // k가 5보다 작으면 배울수 있는 단어 = 0
  cout << res;
}
