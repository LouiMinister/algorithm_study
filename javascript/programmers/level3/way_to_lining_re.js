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
const serialSwap = (array, order) => {
    for (let i = 0; i < order.length; i++){
        const cache = array[i];
        array[i] = array[i + order[i]];
        array[i + order[i]] = cache;
        array = [...array.slice(0,i+1), ...array.slice(i+1).sort((a,b)=>a-b)];
    }
    return array;
}
const nthPermutation = (val, n) => {
    const orderAry = [];
    const recur = (val, n) => {
        const nFac = factorial(n);
        orderAry.push(Math.floor(val/nFac));
        if (n === 1) return;
        recur(val%nFac, n-1);
    }
    recur(val-1, n-1);
    return orderAry;
}
const facMemo = [1,1];
const factorial = n => {
    if (!facMemo[n]) 
        facMemo[n] = n * factorial(n-1);
    return facMemo[n];
}

//----------------------------------------------------------------

const solution_v2 = (n, k) => {
    const ary = Array(n).fill(null).map((_,i)=>i+1);
    return serialSwap_v2(ary, nthPermutation(k, n));
}
const serialSwap_v2 = (array, order) => {
    const result = [];
    array = [...array];
    while(order.length > 0){
        const o = order.shift();
        result.push(array[o]); 
        array.splice(o,1);
    }
    return [...result, array.pop()];
}
(()=>{
    console.log(solution_v2(4,16));
})();





