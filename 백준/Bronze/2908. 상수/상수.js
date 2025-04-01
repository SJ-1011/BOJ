const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(" ");

let A = inputData[0];
let B = inputData[1];

let after_A = "";
let after_B = "";

for (let i = 0; i < 3; i++) {
  after_A = after_A + A[2 - i];
  after_B = after_B + B[2 - i];
}

console.log(Math.max(after_A, after_B));