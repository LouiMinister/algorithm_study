/*
문제 설명
숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. 게임해보기

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.

제한사항
질문의 수는 1 이상 100 이하의 자연수입니다.
baseball의 각 행은 [세 자리의 수, 스트라이크의 수, 볼의 수] 를 담고 있습니다.
입출력 예
baseball	return
[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2
입출력 예 설명
문제에 나온 예와 같습니다.
*/

const solution = (baseball) => {
    const range = new Array(9).fill(null).map((_,i)=>`${i+1}`);
    let candidates = combination(range,3);
    candidates = candidates.filter((candidate)=>
        isCandidate(baseball, candidate));
    return candidates.length;
}
const combination = (arr, n) => {
    const res = [];
    const recursive = (val) => {
        if (val.length === n){
            res.push(val);
            return;
        }
        for (const i of arr){
            if(!val.includes(i)){
                recursive(`${val}${i}`)
            }
        }
    }
    recursive("");
    return res;
}
const swingReuslt = (swing, answer) =>  
    swing.reduce(([ss, sb], s, si) => {
        const [as, ab] = answer.reduce(([as, ab], a, ai) => 
            a == s ?
                ai == si ? 
                    [as+1, ab] : [as, ab+1]
                : [as,ab]
        ,[0,0]);
        return [ss+as, sb+ab];
    },[0,0]);
const isCandidate = (baseball, candidate) => {
    for (const play of baseball){
        const [swing, strike, ball] = play;
        const [sRes, bRes] = swingReuslt([...new String(swing)], [...candidate]);
        if (!(sRes == strike && bRes == ball))
            return false 
    }
    return true;
}

(()=>{
     const baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]];
    //const baseball = [[123, 1, 1]];
    //console.log(swingReuslt([2,1,3],[1,2,3]));
    //console.log(swingReuslt([1,1,1],[1,2,3]));
    //console.log(isCandidate(baseball,'112'));
    //console.log("123".length);
    //console.log(combination([1,2,3,4], 3));
    console.log(solution(baseball));
})();