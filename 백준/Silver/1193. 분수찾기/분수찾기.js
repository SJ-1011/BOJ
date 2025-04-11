const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim();

const X = parseInt(fileData);

// 1: 1
// 2: 2 -> 누적 1 + 2 = 3
// 3: 3 -> 누적 1 + 2 + 3 = 6
// 4: 4 -> 누적 1 + 2 + 3 + 4 = 10

// X = 9면, 3/2(4번째 라인)

let tmp = 1;
let i = 2;
let line = 1;
while (tmp < X) {
  tmp += i;
  i++;
  line++;
}

// tmp - X: 해당 라인에서 몇 번째인지

let arr = [];

// 라인이 짝수라면
if (line % 2 == 0) {
  for (let i = 0; i < line; i++) {
    arr.push(`${line - i}/${i + 1}`);
  }
} else {
  for (let i = 0; i < line; i++) {
    arr.push(`${i + 1}/${line - i}`);
  }
}

console.log(arr[tmp - X]);
