
function main(){
    const ary = [2,1,3,4,5,6,7,8,9];
    solution(ary);
}
function solution(ary) {
    ary = [1];
    console.log(Boolean(ary.length));
    ary.pop();
    console.log(Boolean(ary.length));
    
    
}
main();