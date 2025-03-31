const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/); // 윈도우/리눅스 모두 처리

let T = parseInt(inputData[0]);
let R;
let S;
let result = '';
let line;

for (let i = 1; i <= T; i++){
  line = inputData[i].split(' ');
  R = parseInt(line[0]);
  S = line[1];
  for (let j = 0; j < S.length; j++){
    for (let k = 0; k < R; k++){
      result += S[j];
    }
  }
  console.log(result);
  result = '';
}
