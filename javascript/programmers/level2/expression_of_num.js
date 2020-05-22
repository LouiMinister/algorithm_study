/*

문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
입출력 예
n	result
15	4
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.

*/

const solution2 = (n) => 
    twoNumAry(n).reduce((sum,val) => 
        straightSumFrom(val) === n ? sum+1 : sum
    , 0);
const twoNumAry = (num) => {
    let range = Array.from(new Array(num), (_,i) => i+1);
    return range.reduce((res,start,i) =>
        [...res, ...range.slice(i).reduce((res,end) => 
            [...res, [start, end]]
        ,[])]
    ,[])
}
const solution = (n) => {
    let res = 0;
    for (let i = 1; i <= n; i++){
        let sum = 0;
        for (let j = i; j <= n ; j++){
            sum += j;
            if (sum > n)
                break;
            else if (sum === n)
                sum ++;
        }
    }
    return res;
}
const straightSumIs = ([start, last], n) => {
    let sum = 0;
    for (let i = start; i <= last; i++){
        sum += i;
        if (sum > n)
            break;
    }
    return sum === n ? true : false;
}
const straightMemo = [0,1];
const straightSum = (n) => {
    if (n == 0) return 0;
    if(!straightMemo[n]){
        straightMemo[n] = straightSum(n-1) + n;
    }
    return straightMemo[n];
}
const straightSumFrom = ([start,end],n) => {
    if (end > n/2){
        return start === end ? end : 0 ;
    }
    return straightSum(end) - straightSum(start-1);
}




(()=>{
    const n = 15;
    //console.log(straightSum(3));
    //console.log(twoNumAry(10));
    //console.log(straightSumFrom([1,5]));
    console.log(solution(n));
})();
