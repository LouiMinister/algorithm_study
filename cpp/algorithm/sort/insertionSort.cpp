#include <iostream>

using namespace std;
int arr[10] = {5, 9, 2, 7, 5, 8, 1, 6, 8, 2};

void InsertionSort(int arr[], int n) {
  int j;
  int insVal;
  for (int i = 1; i < n; i++) { // 삽입할 값
    insVal = arr[i];
    for (j = i - 1; j >= 0; j--) { // 삽입할 위치
      if (arr[j] > insVal)
        arr[j + 1] = arr[j];
      else
        break;
    }
    arr[j + 1] = insVal;
  }
}

int main() {
  InsertionSort(arr, 10);
  for (int v : arr)
    cout << v << ' ';
}
