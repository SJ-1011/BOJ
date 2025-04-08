const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

let data;
let arr = [];
const maxNum = new Object();
maxNum.num = 0;
maxNum.x = 0;
maxNum.y = 0;

for (let i = 0; i < 9; i++) {
  data = inputData[i].trim().split(" ");
  arr.push(data.map(Number));
}

for (let i = 0; i < 9; i++) {
  for (let j = 0; j < 9; j++) {
    if (maxNum.num <= arr[i][j]) {
      maxNum.num = arr[i][j];
      maxNum.x = i + 1;
      maxNum.y = j + 1;
    }
  }
}

console.log(maxNum.num);
console.log(maxNum.x, maxNum.y);
