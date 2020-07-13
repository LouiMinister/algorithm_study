const readline = require('readline');
const readLines = async (num = 1) => {
    const res = [];
    const rl = readline.createInterface({
      input: process.stdin
    });
    return new Promise((resolve,reject)=>{
      rl.on('line', (data)=>{
        res.push(data);
        if(res.length == num){rl.close();}
      }).on('close', () =>
		  resolve(res)
	  );
    });
};
const isEqualAry = (targetAry, changeAry) => {
	if (targetAry.length === changeAry.length){
		const len = targetAry.length;
		for(let i = 0; i < len; i++){
			if (targetAry[i] != changeAry[i]){
				return false;
			}
		}
	}
	return true;
};
const overWriteAry = (targetAry, updateAry) => {
	const res = [...targetAry];
	return res.map((val,idx) => val|updateAry[idx]);
};
const getReachableVertexToTarget = (graph, targetVtx) => {
	return graph.reduce((acc,ary,idx)=> {
		if( ary[targetVtx] === 1 ) 
			acc.push(idx);
		return acc;
	},[]);
};
const getReachableGraph = (graph) => {
	const graphLen = graph.length;
	const result = Array(graphLen).fill(null).map( () => Array(graphLen).fill(0));
	const recurUpdate = (targets, updateAry) => {
		for(const target of targets){
			if (!isEqualAry(result[target], updateAry)){
				result[target] = overWriteAry(result[target], updateAry);
				recurUpdate(getReachableVertexToTarget(result, target), result[target]);
			}
		}
	}
	for (let i = 0; i < graphLen; i++){
		recurUpdate([i], graph[i]);
	}
	return result;
};
(async()=>{
	const lines = await readLines();
	const input = await readLines(lines);
    const graph = input.map((val)=>val.split(' ').map(val=>Number(val)));
    const res = getReachableGraph(graph);
    const str = res.map(val=>val.join(' ')).join('\n');
    console.log(str);
})();