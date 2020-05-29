/*
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
 */

const solution = (n) => {
    let res = 0;
    for(let i = 2; i <= n; i++){
        if (isPrime(i)) {
            res++;
        }
    }
    return res;
};
const solution_adv = (n) => {
    const primes = [false, false, ...Array(n-1).fill(true)];
    for(let i = 2; i <= n; i++){
        if (primes[i] === false) continue;
        for(let j = 2; j*i <= n ; j++){
            console.log(j*i);
            primes[j*i] = false;
        }
    }
    console.log(primes);
    return primes.filter(val=>val===true).length;
}

const isPrime = (n) => {
    if (n<2) return false;
    for (let i =2; i <= n/2; i++){
        if (n % i === 0) return false;
    }
    return true;
};

(()=>{
    const n = 50
    console.log(solution_adv(n));
})();
