
(() =>{
    const n = 3;
    const computers = [[1,1,0],[1,1,0],[0,0,1]];

    console.log(solution(n, computers));
})()

function solution(n, computers) {
    let result = 1;
    
    let Node = class Node {
        constructor(number, edge){
            this.number = number;
            this.edge = edge;
            this.checked = false;
        }
    }

    const nodeAry = [];
    computers.forEach((element, index) => {
        nodeAry.push( new Node(index, element) );
    });
    console.log(nodeAry);

    const findUncheckedNodeIndex = (nodeAry) => {
        let result = -1;
        for(let i =0; i<nodeAry.length; i++){
            if(nodeAry[i].checked == false){
                result = i;
                break;
            }
        }
        return result;
    }
    
    const dfsStack = [nodeAry[0]];
    while(true) {

        if(dfsStack.length == 0) {
            const uncheckedNodeIndex = findUncheckedNodeIndex(nodeAry);
            console.log(`uncheckedNode = ${uncheckedNodeIndex}`);
            if (uncheckedNodeIndex >= 0){
                result ++;
                dfsStack.push(nodeAry[uncheckedNodeIndex]);
            } else {
                break;
            }
        }
        console.log(dfsStack);
        const nowNode = dfsStack.pop();
        nowNode.checked = true;
        console.log(nodeAry);
        

        for(let i = 0; i < nowNode.edge.length; i++){

            if(i == nowNode.number){
                continue;
            }

            if(nowNode.edge[i] == 1 && nodeAry[i].checked == false){
                dfsStack.push(nodeAry[i]);
            }
        }
    }
    return result;
    
}