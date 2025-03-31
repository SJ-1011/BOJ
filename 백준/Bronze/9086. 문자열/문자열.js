const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/); // 윈도우/리눅스 모두 처리

const T = parseInt(input[0]);

for (let i = 1; i <= T; i++) {
  const str = input[i]; 
  console.log(str[0] + str[str.length - 1]);
}