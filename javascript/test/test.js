
function main(){
    const ary = [1,1,1,1,1,2,1,1,1,2,1,1,2];
    solution(ary);
}
function solution(ary) {
    let idx =-1;
    while(true){
        idx= ary.indexOf(2,idx+1)

        console.log(idx);
    }
    
}
main();