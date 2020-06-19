const combination = (n, r) => {
	if (n === 0 || r === 0 || n < r){ return undefined; } 
	const res = [];
	const candidate = Array(n).fill(null).map((_,i)=>i);
	const recur = (n, r, candidate, val) => {
		if (r === 0) {
			res.push(val);
			return;
		}
		if (n === r) {
			res.push([...val, ...candidate]);
			return;
        }
        // nCr = (n-1)Cr + (n-1)C(r-1)
		recur(n-1, r-1, candidate.slice(1), [...val,candidate[0]]);
		recur(n-1, r, candidate.slice(1), [...val]);
	}
	recur(n, r, candidate, []);
	return res;
}