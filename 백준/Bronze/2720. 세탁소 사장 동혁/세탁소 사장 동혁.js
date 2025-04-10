const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

const T = Number(fileData[0]);
let C;
let Q, D, N, P;
let tmp;

for (let i = 1; i < fileData.length; i++) {
  C = parseInt(fileData[i]);
  Q = parseInt(C / 25);
  tmp = C % 25;
  D = parseInt(tmp / 10);
  tmp = tmp % 10;
  N = parseInt(tmp / 5);
  tmp = tmp % 5;
  P = parseInt(tmp / 1);
  tmp = tmp % 1;

  console.log(Q, D, N, P);
}
