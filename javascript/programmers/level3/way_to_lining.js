/*
문제 설명
n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

제한사항
n은 20이하의 자연수 입니다.
k는 n! 이하의 자연수 입니다.
입출력 예
n	k	result
3	5	[3,1,2]
입출력 예시 설명
입출력 예 #1
문제의 예시와 같습니다.
*/

const solution = (n, k) => {
    const ary = Array(n).fill(null).map((_,i)=>i+1)
    return serialSwap(ary, nthPermutation(k, n));
}

const swapPermutation = (array) => {
    const result = [];
    const recur = (array, [a,b]) => {
        array = [...array];
        for (let i = a; i <= b ; i++){
            const cache = array[a];
            array[a] = array[i];
            array[i] = cache;
            console.log(`${array} ${a} ${b}`);
            a+1 === b ? result.push([...array]) : recur(array, [a+1,b]);
        }
    }
    recur(array, [0, array.length-1]);
    return result;
}
const serialSwap = (array, order) => {
    array = [...array];
    for (let i = 0; i < order.length; i++){
        const cache = array[i];
        array[i] = array[i + order[i]];
        array[i + order[i]] = cache;
    }
    return array;
}
const nthPermutation = (val, n) => {
    const orderAry = [];
    const recur = (val, n) => {
        const nFac = factorial(n);
        orderAry.push(Math.floor(val/nFac));
        if (n === 1 ) return;
        recur(val%nFac, n-1);
    }
    recur(val-1, n-1);
    console.log(orderAry);
    return orderAry;
}
const facMemo = [1,1];
const factorial = n => {
    if (!facMemo[n]) 
        facMemo[n] = n * factorial(n-1);
    return facMemo[n];
}

(()=>{
    //console.log(swapPermutation([1,2,3]));
    //console.log(nthPermutation([1,2,3,4],24,4));
    console.log(solution(3,5));
})();





