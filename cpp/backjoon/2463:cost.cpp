#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1000000000;

vector<vector<int>> vertex;  // V
int parent[112345];          // N
long long sizeOfSet[112345]; // N
int N, V;
long long vertexSum = 0;
long long res = 0;

bool cmp(const vector<int> &a, const vector<int> &b) { return a[2] > b[2]; }

int findRoot(int node) {
  if (parent[node] == node) {
    return node;
  }
  return parent[node] = findRoot(parent[node]);
}

void unite(int a, int b) {
  int aRoot = findRoot(a);
  int bRoot = findRoot(b);

  if (aRoot != bRoot) {
    parent[aRoot] = parent[bRoot];
    sizeOfSet[bRoot] += sizeOfSet[aRoot];
    sizeOfSet[aRoot] = 1;
  }
}

int main() {
  cin >> N >> V;
  vertex.resize(V, vector<int>(3));
  for (int i = 0; i < V; i++) {
    cin >> vertex[i][0] >> vertex[i][1] >> vertex[i][2];
    vertexSum += vertex[i][2];
  }
  sort(vertex.begin(), vertex.end(), cmp);
  for (int i = 1; i <= N; i++) {
    parent[i] = i;
    sizeOfSet[i] = 1;
  }

  for (vector<vector<int>>::iterator i = vertex.begin(); i != vertex.end();
       i++) {
    int nodeA = i->at(0);
    int nodeB = i->at(1);
    int aRoot = findRoot(nodeA);
    int bRoot = findRoot(nodeB);
    if (aRoot != bRoot) {
      long long cnt = (sizeOfSet[aRoot] * sizeOfSet[bRoot]);
      res += (cnt * vertexSum);
      res %= MOD;
      unite(nodeA, nodeB);
    }
    vertexSum -= i->at(2);
  }
  cout << res;
}
