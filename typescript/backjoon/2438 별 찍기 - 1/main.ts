/*
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
*/
import fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let input = '1'.toString().split(' ');
const max = Number(input[0]);
for(let i = 1; i <= max; i++){
  console.log('*'.repeat(i));
}