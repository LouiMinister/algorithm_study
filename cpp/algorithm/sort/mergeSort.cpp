#include <iostream>

using namespace std;
int arr[10] = {5, 9, 2, 7, 5, 8, 1, 6, 8, 2};

int cache[10];
void mergeAry(int a[], int left, int mid, int right) {
  int i = left;
  int j = mid + 1;
  int k = 0;
  while (i <= mid && j <= right) {
    if (a[i] <= a[j])
      cache[k++] = a[i++];
    else
      cache[k++] = a[j++];
  }
  copy(a + i, a + mid + 1, cache + k);
  copy(a + j, a + right + 1, cache + k);
  copy(cache, cache + (right - left) + 1, a + left);
}

void MergeSort(int a[], int left, int right) {
  if (left >= right)
    return;
  int mid = (left + right) / 2;
  MergeSort(a, left, mid);
  MergeSort(a, mid + 1, right);
  mergeAry(a, left, mid, right);
}

int main() {
  MergeSort(arr, 0, 9);
  for (int v : arr)
    cout << v << ' ';
}
