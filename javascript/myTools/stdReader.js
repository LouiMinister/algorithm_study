const readline = require('readline');

const getStdMultiInput = async (numOfEachLine) => {
    const res = {
        cases: null,
        numOfEachLine: numOfEachLine,
        inputs: []
    };

    const rl = readline.createInterface({
       input: process.stdin,
       output: process.stdout 
    });
    const ary = [];

    return new Promise((resolve, reject)=>{
        rl.on('line', (line)=>{
            ary.push(line);
            if (line === "q") {
                rl.close();
            }
            rl.setPrompt(4);
            rl.prompt();
        })
           .on('close', ()=>{
            console.log("closed");
            resolve(ary);
        });
    });
    
}
/*
const readLines = (maxLine) => {
    const res = [];
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.on('line', (line) => {
        res.push(line)
        if (res.length === maxLine){
            rl.close();
        }
    })
      .on('close', () => {
        return res;
      });
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input.push(line)
    if(line ==='q'){
        rl.close();
    }
  })
  .on('close', function () {
    console.log(`close  ${input}`);
});

console.log(`end`);
*/
const sum = (a,b) => {return a+b;};
//process.stdout.write('data');
(async() => {
    console.log(await getStdMultiInput(1));
})();

console.log("end");

setTimeout(()=>process.stdout.write('data'),1000);

export{sum}