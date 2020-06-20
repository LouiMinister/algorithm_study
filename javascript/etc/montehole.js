const getRandom = (max, without = []) => {
    const arange = new Array(max + without.length).fill(null).map((_,idx)=>idx);
    let n = Math.random() * max;
    for(const n of without){
        arange.splice(arange.indexOf(n),1);
    }
    return arange[Math.floor(n)];
}

const res = [0,0];
let n = 1000000;
while(n--){
    const door = ["goat","goat","goat"];
    door[getRandom(3)] = "car";

    let playerSelect = getRandom(3);
    let adminSelect;
    if(door[playerSelect] === "goat"){
        adminSelect = getRandom(1,[playerSelect, door.indexOf("car")]);
    } else {
        adminSelect = getRandom(2, [playerSelect]);
    }
    
    playerSelect = getRandom(1,[playerSelect, adminSelect]);
    if (door[playerSelect] === "car") {
        res[0]++;
    } else {
        res[1]++;
    }
}
console.log(`정답을 맞춘 수 : ${res[0]} 틀린 수 : ${res[1]}`);