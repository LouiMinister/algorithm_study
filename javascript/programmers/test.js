
function main(){
    const ary = [2,1,3,4,5,6,7,8,9];

    // [...ary].forEach((val, idx) =>{
    //     console.log(`val: ${val}, ary[${idx}]: ${ary[idx]}`);
    //     //ary.shift();
    //
    //     ary.pop();
    //     console.log(`val: ${val}, ary[${idx}]: ${ary[idx]}`);
    // });

   console.log(ary.sort((a,b)=>NaN));

}
function solution(seoul) {
    return `김서방은 ${seoul.findIndex(value => (value === "Kim") ? true : false)}에 있다`;
}
main();