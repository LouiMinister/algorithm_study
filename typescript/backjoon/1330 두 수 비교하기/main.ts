/*
A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
*/
import fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let input: any = '1 2'.toString().split(' ');
const [a, b] = input.map((val: any) => Number(val));
if (a > b) {
  console.log('>');
} else if (a < b) {
  console.log('<');
} else {
  console.log('==');
}