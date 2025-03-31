const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/); // 윈도우/리눅스 모두 처리

let N = parseInt(inputData[0]);
let sum = 0;
for (let i = 0; i < N; i++){
  sum += parseInt(inputData[1][i]);
}
console.log(sum);