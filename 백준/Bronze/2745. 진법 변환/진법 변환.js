const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim().split(" ");
const N = fileData[0];
const B = fileData[1];

let tmp;
let arr = [];

for (let i = 0; i < N.length; i++) {
  if (isNaN(N[i])) {
    tmp = N[i].toUpperCase().charCodeAt(0) - 55;
  } else {
    tmp = N[i];
  }
  arr.push(tmp);
}

let num = arr.length - 1;
let ans = 0;

for (let i = 0; i < arr.length; i++) {
  tmp = Number(B) ** num--;
  ans += arr[i] * tmp;
}

console.log(ans);
