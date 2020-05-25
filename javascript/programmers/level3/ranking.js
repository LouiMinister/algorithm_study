/*
###### 문제 설명

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 선수의 수는 1명 이상 100명 이하입니다.
- 경기 결과는 1개 이상 4,500개 이하입니다.
- results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
- 모든 경기 결과에는 모순이 없습니다.

##### 입출력 예

| n    | results                                  | return |
| ---- | ---------------------------------------- | ------ |
| 5    | [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]] | 2      |

##### 입출력 예 설명

2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.

|      |      |      |
| ---- | ---- | ---- |
|      |      |      |
|      |      |      |
[[[2,3],[4,5]],[[1,5],[3,6]]
*/

const solution = (n, results) => {
    let table = newTable(n);
    for (const result of results){
        table = setTable(result, table);
    }
    return numOfFilledRow(calculate(table));
}
const numOfFilledRow = table => 
    table.reduce((sum, row) => {
        for (const val of row) {
            if (val === null) return sum;
        }
        return sum + 1;
    }, 0);

const calculate = table => {
    let recursive = false;
    const result = table.reduce((acc, row) => {
        const winLose = row.reduce((winLose, val, idx) => {
            if (val === 1 ) winLose[0].push(idx+1);
            if (val === -1) winLose[1].push(idx+1);
            return winLose; 
        }, [[],[]]);
        for (const win of winLose[0]){
            for (const lose of winLose[1]){
                if (acc[lose-1][win-1] === null) recursive = true;
                acc[lose-1][win-1] =  1;
                acc[win-1][lose-1] = -1;
            }
        }
        return acc;
    },[...table].map(val => [...val]));
    return recursive === true ? calculate(result) : result;
}
const newTable = (n) => {
    const table = new Array(n).fill(null).map(_=>new Array(n).fill(null));
    for (let i = 0; i < table.length; i++){
        table[i][i] = 0;
    }
    return table;
}
const setTable = ([win, loose], table) => {
    table = [...table].map(val => [...val]);
    table[win-1][loose-1] = 1;
    table[loose-1][win-1] = -1;
    return table;
}

(()=>{
    const n = 5;
    const results =  [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]];
    //const results =  [[1, 2], [2, 4], [4, 3], [3, 5], [2, 5]];
    //console.log(setTable([1,2],new Array(6).fill(new Array(6))));
    console.log(solution(n,results));
    // console.log(calculate([
    //     [ 0, 1, null, null, null ],
    //     [ -1, 0, -1, -1, 1 ],
    //     [ null, 1, 0, -1, null ],
    //     [ null, 1, 1, 0, null ],
    //     [ null, -1, null, null, 0 ]
    //   ]));
})();