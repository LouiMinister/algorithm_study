/*
문제 설명
가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다. 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다. 타일을 채울 때는 다음과 같이 2가지 방법이 있습니다.

타일을 가로로 배치 하는 경우
타일을 세로로 배치 하는 경우

직사각형의 가로의 길이 n이 매개변수로 주어질 때, 이 직사각형을 채우는 방법의 수를 return 하는 solution 함수를 완성해주세요.

제한사항
가로의 길이 n은 60,000이하의 자연수 입니다.
경우의 수가 많아 질 수 있으므로, 경우의 수를 1,000,000,007으로 나눈 나머지를 return해주세요.
*/

(function main(){
    n = 6;

    console.log(solution(n));
})();

function solution(n) {
    const param_n = n;

    const number_of_case_by_num_of_onetwo = [];
    for(let number_of_2=0; number_of_2 <= param_n/2; number_of_2++){
        const number_of_1 = param_n - number_of_2 * 2;
        const case_by_num_of_onetwo = new Map()
            .set(1,number_of_1)
            .set(2,number_of_2);
        number_of_case_by_num_of_onetwo.push(case_by_num_of_onetwo);
    }

    const factorial_memo_ary = [];
    const _factorial = (n) => factorial(n, factorial_memo_ary);
    console.log(number_of_case_by_num_of_onetwo);
    const number_of_case = number_of_case_by_num_of_onetwo
        .reduce( (sum_of_case, current_case) => {
            const number_of_1 = current_case.get(1);
            const number_of_2 = current_case.get(2);
            const current_number_of_case = 
                _factorial(number_of_1 + number_of_2) /
                (_factorial(number_of_1) * _factorial(number_of_2));
            console.log(current_number_of_case)
            sum_of_case += current_number_of_case;
            return sum_of_case;
        },0);

    return number_of_case;
}

function factorial(n, memo_ary){
    if (n == 0 || n == 1)
        return 1;
    if (memo_ary[n] > 0)
        return memo_ary[n];
    return memo_ary[n] = factorial(n-1, memo_ary) * n;
}