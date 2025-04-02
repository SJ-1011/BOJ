const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();

let p = 0;
let q = inputData.length - 1;
let ans = 1;

while (p <= q) {
  if (inputData[p] != inputData[q]) {
    ans = 0;
    break;
  }
  p++;
  q--;
}

console.log(ans);
