/*
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
*/

function solution(arr1, arr2) {
    //const w1h2 = arr1[0].length;
    //const h1 = arr1.length;
    //const w2 = arr2[0].length;
    const res = new Array(arr1.length).fill(null).map(_ => 
        new Array(arr2[0].length).fill(null));
    return res.map((row,j)=> 
        row.map((_,i) => {
            let sum = 0;
            for(let k = 0; k < arr1[0].length; k++)
                sum += arr1[j][k] * arr2[k][i];
            return sum;
        })
    )
}
function solution2(arr1, arr2) {
    return arr1.map((row) => arr2[0].map((x,y) => row.reduce((a,b,c) => a + b * arr2[c][y], 0)))
}
(()=>{
    const arr1 = [[1, 4], [3, 2], [4, 1]];
    const arr2 = [[3, 3], [3, 3]];
    console.log(solution2(arr1,arr2));
})();























