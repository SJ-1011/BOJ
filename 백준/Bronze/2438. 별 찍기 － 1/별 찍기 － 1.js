const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

const t = parseInt(inputData[0]);

let ans = "";
for (let i = 1; i <= t; i++) {
  for (let j = 0; j < i; j++) {
    ans += "*";
  }
  console.log(ans);
  ans = "";
}
