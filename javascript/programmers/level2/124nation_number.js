// 문제 설명
// 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
//
// 124 나라에는 자연수만 존재합니다.
// 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
//     예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
//
// 10진법	124 나라	10진법	124 나라
// 1	1	6	14
// 2	2	7	21
// 3	4	8	22
// 4	11	9	24
// 5	12	10	41

// 0	0	5	21
// 1	1	6	02
// 2	2	7	12
// 3	01	8	22
// 4	11	9	03

/*
 1x1
 1x2
 1x3
 1x1+ 3x1
 1x2+ 3x1
 1x3+ 3x1

 41 = 9*3 + 3*3 + 3*1 + 1*2
 */
//
// 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
//
//     제한사항
// n은 500,000,000이하의 자연수 입니다.
//     입출력 예
// n	result
// 1	1
// 2	2
// 3	4
// 4	11
(function main(){
    number = 6;

    console.log(solution(number));
})();

function solution(number) {
    // 3의 n 승으로 나눌 때 최대의 값 n을 구함

    // number을 3의 n승, n-1승, n-2승 ... 0 승까지 나눔
    // number5 = 3^5 * n + r => [].push(n)

    let maxLevel = 0;
    let maxValue = 1;
    while(true){
        console.log(maxValue);
        if(number > maxValue * 3){
            maxValue *= 3;
            maxLevel ++;
        } else {
            break;
        }
    }

    const ary = [];
    for(maxLevel ; maxLevel >= 0 ; maxLevel--){
        if (number == 0){
            ary[maxLevel] = 0;
            continue;
        }

        let multi = parseInt(number / maxValue );
        if(multi != 0 ) {
            let rest = number % (maxValue * multi);
            ary[maxLevel] = multi;
            number = rest;
        } else {
            ary[maxLevel] = 0;
        }
        maxValue = parseInt(maxValue / 3);
        console.log(`number : ${number} maxValue : ${maxValue} multi : ${multi}`);
        console.log(ary);
    }
    console.lg
    ary.reduce((prev, current, index) => {
        switch (current) {
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
        }
    },"")
}