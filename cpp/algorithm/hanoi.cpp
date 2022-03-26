#include <iostream>

using namespace std;

void Hanoi(int n, char from, char by, char to) {
  if (n == 1) {
    cout << from << "=>" << to << endl;
  } else {
    Hanoi(n - 1, from, to, by);
    Hanoi(1, from, by, to);
    Hanoi(n - 1, by, from, to);
  }
}

int main() { Hanoi(3, 'A', 'B', 'C'); }
