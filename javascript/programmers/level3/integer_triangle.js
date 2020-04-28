

(() =>{
    const triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]];
    
    console.log(solution(triangle));
    console.log(triangle);
})()

function solution(triangle) {
    triangle = [...triangle];
    for(let floor = triangle.length-2; floor >=0; floor--){
        triangle[floor].forEach( (upNum, idx) =>{
            const leftDownNum = triangle[floor+1][idx];
            const rightDownNum = triangle[floor+1][idx+1];
            triangle[floor][idx] += 
                leftDownNum > rightDownNum ? leftDownNum : rightDownNum;
        });
        console.log(triangle);
    }
    return triangle[0][0];
}

