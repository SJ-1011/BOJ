const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

let num = Number(inputData[0]);
let data;
let arr = [];

for (let i = 1; i <= num; i++) {
  data = inputData[i].trim().split(" ").map(Number);
  arr.push(data);
}

let ans = [];
let temp;
let cnt = 0;

for (let i = 0; i < 100; i++) {
  temp = [];
  for (let j = 0; j < 100; j++) {
    temp.push(0);
  }
  ans.push(temp);
}

for (let i = 0; i < num; i++) {
  for (let j = 0; j < 10; j++) {
    for (let k = 0; k < 10; k++) {
      if (ans[arr[i][0] + j][arr[i][1] + k] == 1) {
        continue;
      } else {
        ans[arr[i][0] + j][arr[i][1] + k] = 1;
        cnt++;
      }
    }
  }
}
console.log(cnt);