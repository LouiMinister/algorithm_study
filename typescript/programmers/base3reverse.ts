function convertBaseNum(base: number, n: number) : number {
    let result : string = "";
    while (n >= base){
        let remainder : number;
        remainder = n % base;
        n = (n - remainder) / base;
        result = remainder.toString() + result;
    }
    result = n.toString() + result;
    return Number(result);
}

console.log(convertBaseNum(3, 78));