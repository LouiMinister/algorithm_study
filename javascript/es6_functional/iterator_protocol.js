const {log} = console

// 이터레이터 프로토콜을 다르는 map
const map = (f, iter) => {
    const res = [];
    for (const val of iter){
        res.push(f(val));
    }
    return res;
}

// 이터레이터 프로토콜을 따르는 filter
const filter = (f, iter) => {
    const res = [];
    for (const val of iter){
        if (f(val)) res.push(val); 
    }
    return res;
}

// 이터레이터 프로토콜을 따르는 reduce
const reduce = (f, acc, iter) => {
    if(!iter){
        iter = acc[Symbol.iterator]();
        acc = iter.next().value;
    }
    for (const val of iter){
         acc = f(acc, val);
    }
    return acc;
}

// unit test
log(map(a=>a+1, [1,2,3,4,5]));
log(filter(a=> a%2 === 1, [1,2,3,4,5]));
log(reduce((acc,a)=>acc+a, 100, [1,2,3,4,5]));
log(reduce((acc,a)=>acc+a, [1,2,3,4,5]));