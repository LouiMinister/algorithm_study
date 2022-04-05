#include "rectangle.h"
#include <iostream>

using namespace std;

Rectangle::Rectangle() {
  width = 0;
  height = 0;
}
Rectangle::Rectangle(int width, int height) {
  this->width = max(width, 0);
  this->height = max(height, 0);
}
int Rectangle::area() { return width * height; }
int Rectangle::perimeter() { return 2 * (width + height); }
