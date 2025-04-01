const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

let arr = inputData[0].split(" ");
let H = parseInt(arr[0]);
let M = parseInt(arr[1]);
let time = parseInt(inputData[1]);

M = M + time;

if (M >= 60) {
  H = H + Math.floor(M / 60);
  M = M % 60;
}
if (H >= 24) {
  H = H % 24;
}

console.log(H, M);
