/*
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
*/
import fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let input = '2'.toString().split('')[0];
for(let i = 1 ; i <= 9; i++ ){
    //2 * 3 = 6
  console.log(`${input} * ${i} = ${Number(input)*i}`);
}
