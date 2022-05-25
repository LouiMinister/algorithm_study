#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits.h>
#include <queue>
#include <vector>

using namespace std;
const int NODECNT = ('Z' - 'A' + 1) * 2;
int E;
int cap[NODECNT][NODECNT];  // graph (capacity)
int flow[NODECNT][NODECNT]; // 흐름
int visitedBy[NODECNT];

int ctoi(char c) {
  if (c <= 'Z') {
    return c - 'A';
  } else {
    return c - 'a' + 26;
  }
}

int *bfs(int sNode, int eNode) { // 시작노드, 끝노드
  fill_n(visitedBy, NODECNT, -1);
  queue<int> q;
  q.push(sNode);
  visitedBy[sNode] = sNode;
  while (!q.empty()) {
    int nowNode = q.front();
    q.pop();
    for (int toNode = 0; toNode < NODECNT; toNode++) {
      int capacity = cap[nowNode][toNode];
      if (capacity == 0) // 인접한 노드가 아닐경우
        continue;
      int leftFlow = capacity - flow[nowNode][toNode];
      if (visitedBy[toNode] == -1 &&
          leftFlow > 0) { //방문 안한 노드 & 잔여 용량 존재
        q.push(toNode);
        visitedBy[toNode] = nowNode;
        if (toNode == eNode)
          return visitedBy;
      }
    }
  }
  return 0; // 경로가 없는 경우
}

int edmond(int sNode, int eNode) {
  int flowSum = 0;
  while (true) { // bfs 해서 경로가 존재하지 않을 떄 까지 반복
    int *visitedBy = bfs(sNode, eNode);
    if (visitedBy == 0) // 더 이상 경로가 없는 경우
      break;
    int pipeFlow = INT_MAX;
    int nowNode = eNode; // 현재 노드 (최초: 마지막노드)
    while (true) {       // bfs 결과 경로 순회 -> pipeFlow 연산
      int prevNode = visitedBy[nowNode]; // 이전 노드
      if (nowNode == prevNode) // 최초 노드가 현재 노드인 경우
        break;
      pipeFlow =
          min(pipeFlow, cap[prevNode][nowNode] - flow[prevNode][nowNode]);
      nowNode = prevNode;
    }

    nowNode = eNode; // 현재 노드 (최초: 마지막노드)
    while (true) {   // bfs 결과 경로 순회 -> flow update
      int prevNode = visitedBy[nowNode]; // 이전 노드
      if (nowNode == prevNode) // 최초 노드가 현재 노드인 경우
        break;
      flow[prevNode][nowNode] += pipeFlow;
      flow[nowNode][prevNode] += -pipeFlow;
      nowNode = prevNode;
    }
    flowSum += pipeFlow;
  }
  return flowSum;
}

int main() {
  cin >> E;
  char in1, in2;
  int in3;
  for (int i = 1; i <= E; i++) {
    cin >> in1 >> in2 >> in3;
    cap[ctoi(in1)][ctoi(in2)] += in3;
    cap[ctoi(in2)][ctoi(in1)] += in3;
  }
  cout << edmond(ctoi('A'), ctoi('Z'));
}
