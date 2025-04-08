const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

let data;
let arr = [];

for (let i = 0; i < 5; i++) {
  data = inputData[i].trim().split("");
  arr.push(data);
}

data = "";

// 배열의 길이 구하기
let maxLen = 0;
for (let i = 0; i < 5; i++) {
  if (maxLen <= arr[i].length) {
    maxLen = arr[i].length;
  }
}

for (let i = 0; i < maxLen; i++) {
  for (let j = 0; j < 5; j++) {
    if (!arr[j][i]) {
      continue;
    }
    data += arr[j][i];
  }
}

console.log(data);
