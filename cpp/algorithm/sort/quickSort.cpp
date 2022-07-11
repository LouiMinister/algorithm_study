
#include <iostream>

using namespace std;
int a[10] = {3, 3, 3};

void QuickSort(int a[], const int left, const int right) {
  if (left >= right)
    return;
  int low = left + 1;
  int high = right;
  int pivot = left;
  while (low <= high) {
    while (low <= right && a[low] <= a[pivot])
      low++;
    while (high > left && a[high] >= a[pivot])
      high--;
    if (low > high)           // low high가 엇갈린 경우 -> 검사 끝
      swap(a[left], a[high]); // 이 때는 high가 작은 값
    else // 아닌 경우 -> 양쪽 부분집합에 값 바꿔 넣어주고 검사 진행
      swap(a[low], a[high]);
  }
  QuickSort(a, left, high - 1); // 피벗 high랑 스왑했으므로 high 기준
  QuickSort(a, high + 1, right);
}

int main() {
  QuickSort(a, 0, 3 - 1);
  for (int v : a)
    cout << v << ' ';
}
