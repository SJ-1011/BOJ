const fs = require("fs");
const S = fs.readFileSync(0).toString().trim(); // 윈도우/리눅스 모두 처리

let arr = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, ];
let num;

for (let i = 0; i < S.length; i++){
  num = S[i].charCodeAt() - 97;
  if (arr[num] == -1) {
    arr[num] = i;
  }
}

console.log(arr.join(" "));