const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

const t = parseInt(inputData[0]);

let ans = "";
for (let i = 1; i <= t; i++) {
  for (let j = t - 1; j >= i; j--) {
    ans += " ";
  }
  for (let k = 1; k <= i; k++) {
    ans += "*";
  }
  console.log(ans);
  ans = "";
}