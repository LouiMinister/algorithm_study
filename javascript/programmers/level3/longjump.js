/*
문제 설명
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

제한 사항
n은 1 이상, 2000 이하인 정수입니다.
입출력 예
n	result
4	5
3	3
입출력 예 설명
입출력 예 #1
위에서 설명한 내용과 같습니다.

입출력 예 #2
(2칸, 1칸)
(1칸, 2칸)
(1칸, 1칸, 1칸)
총 3가지 방법으로 멀리 뛸 수 있습니다.
 */

/*

    길이가 4일 떄 2~4
        4: 14    [4,0] : 4!/4!
        3: 12 21 [2,1] : 3!/2!*1!
        2: 22    [0,2] : 2!/2!

    길이가 5일 때 3~5
        5: 15    [5,0] : 5!/5!
        4: 13 21 [3,1] : 4!/3!
        3: 11 22 [1,2] : 3!/2!

    길이가 n일 때
        짝수 : n/2 ~ n
        홀수 : n/2 + 1 ~ n

1 1
2 2
3 3
4 5
5 8
*/


(()=>{
    const n =4;
    console.log(solutionDP(n));
})();


function factorial(n, k=1){
    let result = 1;
    for(let i=n; i>k; i--){
        result *= i;
    }
    return result;
}

function solution(n) {
    let way = [n,0];
    let result = 0;
    while(way[0] >= 0){
        result +=  way[0] > way[1] ?
            factorial(way[0]+way[1], way[0]) / factorial(way[1])
            : factorial(way[0]+way[1], way[1]) / factorial(way[0]);
        way[0] -= 2;
        way[1]++;
    }

    return result%1234567;
}

function solutionDP(n) {
    const dp = [,1,2];
    const dpFunc = (n) => {
        if (n<=2)
            return dp[n];
        if (!dp[n])
            dp[n] = dpFunc(n-1) + dpFunc(n-2);
        return dp[n];
    };
    return dpFunc(n);
}

