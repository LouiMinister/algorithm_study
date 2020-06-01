
/*
    문제 설명
    JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

    제한 조건
    s는 길이 1 이상인 문자열입니다.
    s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
    첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
    입출력 예
    s	return
    3people unFollowed me	3people Unfollowed Me
*/
const solution = (s) => 
    [...s].map((char ,index) => {
        if (index >= 0 && (s[index-1] === " " || index === 0)) {
            const charCode = char.codePointAt(0);
            console.log(charCode);
            if (charCode >= 97 && charCode <= 122){
                console.log(char);
                return char.toUpperCase();
            } else {
                return char.toLowerCase();
            }
        }
        return char
    }).join("");

(()=>{
    const s = "people Unfollowed Me";
    console.log(solution(s));
})();