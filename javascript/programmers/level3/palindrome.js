/*

###### 문제 설명

앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.

예를들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.

##### 제한사항

- 문자열 s의 길이 : 2,500 이하의 자연수
- 문자열 s는 알파벳 소문자로만 구성

------

##### 입출력 예

| s       | answer |
| ------- | ------ |
| abcdcba | 7      |
| abacde  | 3      |

##### 입출력 예 설명

입출력 예 #1
4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.

입출력 예 #2
2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.ㅔㅁ

*/

(()=>{
    //const s = "abcdcba";
    const s ="abcdcba";
    console.log(solution_r(s));
    //console.log(solution(s));
})();

function solution(s)
{
    let result = 1;
    const isPalindrome = (string) => {
        string = [...string];
        const len = string.length;
        const centerNum = len/2-1;
        for (let i =0; i<=centerNum; i++){
            if (string[i] != string[len-1-i]) 
                return false; 
        }
        return true;
    }
    s = [...s];
    const len = s.length;
    for(let i=0; i<len; i++){
        for(let k=0; k<2; k++){
            for(let j=0; i-j >=0 && i+j+1+k<=len; j++){
                if(2*j+1+k <= result) 
                    continue;
                console.log(`${i-j} ${i+j+1+k} ${s.slice(i-j, i+j+1+k)}`);
                if (isPalindrome(s.slice(i-j, i+j+1+k))){
                    result = 2*j+1+k;
                    console.log(true);
                } else {
                    break;
                }
            }
        }
    }
    return result;
}

//reverse 이용한 풀이
function solution_r(s){
    const len = s.length;
    if (s === s.split("").reverse().join(""))
        return len;
    else {
        const A = solution_r(s.slice(0,len-1));
        const B = solution_r(s.slice(1,len));
        return Math.max(A,B);
    }
}

