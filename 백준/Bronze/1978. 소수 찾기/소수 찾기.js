const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);

let N = Number(input[0]);
let numList = input[1].split(" ").map(Number);
let cnt = 0;
let flag;

for (let i = 0; i < N; i++) {
  flag = true;

  for (let j = 2; j < numList[i]; j++) {
    if (numList[i] % j == 0) {
      flag = false;
      break;
    }
  }
  if (numList[i] == 1) flag = false;
  if (flag) {
    cnt++;
  }
}

console.log(cnt);
