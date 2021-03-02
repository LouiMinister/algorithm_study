/*

*/
import fs = require('fs');
function main() {
    //let input = fs.readFileSync('/dev/stdin').toString().split(' ');
    let input = '8 7 6 5 4 3 2 1'.toString().split(' ').map(val => Number(val));
    let prevSorted;
    for (let i = 1; i < input.length; i++) {
        let nowSorted = ''
        if (input[i - 1] < input[i]) {
            nowSorted = 'ascending';
        } else if (input[i - 1] > input[i]) {
            nowSorted = 'descending';
        }
        if (prevSorted && prevSorted != nowSorted) {
            return 'mixed';
        }
        prevSorted = nowSorted;
    }
    return prevSorted;
}
console.log(main());