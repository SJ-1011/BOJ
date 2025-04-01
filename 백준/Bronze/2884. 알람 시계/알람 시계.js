const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(" ");

let H = inputData[0];
let M = inputData[1];

M = M - 45;

if (M < 0) {
  H = H - 1;
  M = M + 60;
}
if (H < 0) {
  H = H + 24;
}

console.log(H, M);