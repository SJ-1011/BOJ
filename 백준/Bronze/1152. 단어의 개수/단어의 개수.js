const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim(); // 윈도우/리눅스 모두 처리

let arr = inputData.split(' ');
let answer = arr.length;

for (let i = 0; i < arr.length; i++){
  if (arr[i] == '') {
    answer -= 1;
  }
}

console.log(answer);