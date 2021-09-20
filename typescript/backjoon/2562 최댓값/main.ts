/*

*/
import fs = require('fs');
//let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let input = `3
29
38
12
57
74
40
85
61`.toString().split('\n').map(val=>Number(val));
let max = Number.MIN_SAFE_INTEGER;
let maxI = 0;
for( let i = 0; i < input.length; i++){
    if (max<input[i]){
        max = input[i];
        maxI = i+1;
    }
}
console.log(max);
console.log(maxI);
