

//진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.

const solution = (n, t, m, p) => {
    let str = "";
    let num = 0;
    while (t * m >= str.length){
        str = str.concat(num.toString(n));
        num++;
    }
    console.log(m,p,1);
    console.log(isMyTurn(m,p,1));
    return [...str].reduce((res,char,index) => 
        isMyTurn(m,p,index+1) ? res.concat(char) : res
    ,"").slice(0,t).toUpperCase();
}

// 게임 참가 인원 m, 튜브의 순서 p, 턴수 r
const isMyTurn = (m, p, r) => 
    p % m === r % m ? true : false;


(()=>{

 

    console.log(solution(16,16,2,2));
})();