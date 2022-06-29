#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

priority_queue<int> pq;

int solution(vector<int> scoville, int K) {
  int answer = 0;

  for (int v : scoville) {
    pq.push(-v);
  }

  int a, b;
  while (-pq.top() < K) {
    if (pq.size() == 1)
      return -1;
    a = -pq.top();
    pq.pop();
    b = -pq.top();
    pq.pop();
    pq.push(-(a + b * 2));
    answer++;
  }
  return answer;
}
