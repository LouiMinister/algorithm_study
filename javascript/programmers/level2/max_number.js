
/*
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	return
[6, 10, 2]	6210
[3, 30, 34, 5, 9]

[3, 143, 2, 24, 52, 342, 5]

[3, 142, 2, 24, 52, 342, 5] => 52, 5 비교 : 2랑 나머지 숫자들의 첫숫자 비교 : 2 랑 5 비교



*/

function main(){
    const numbers = [3, 142, 2, 24, 52, 342, 5];

    console.log(solution(numbers));
}
function solution(numbers) {
    console.log(String(3).charAt(1) == "");

    const s_numbers = numbers.sort((a,b)=>{
        let index = 0;
        const aStr = String(a);
        const bStr = String(b);
        while(true){
            console.log(`${aStr.charCodeAt(index)} - ${bStr.charCodeAt(index)}`)
            const aChar = aStr.charCodeAt(index);
            const bChar = bStr.charCodeAt(index);

            let cmp =  aChar - bChar;

            if(isNaN(aChar) && isNaN(bChar)){
                return 0;
            }

            if(cmp == 0){
                index++
            } else {
                return -cmp;
            }
        }
    });

    console.log(s_numbers);

}
main();