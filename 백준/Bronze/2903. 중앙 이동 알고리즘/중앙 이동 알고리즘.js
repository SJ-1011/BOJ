const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim();

const N = Number(fileData);

const start = 2;
let ans = start;

for (let i = 0; i < N; i++) {
  ans = (ans - 1) * 2 + 1;
}

console.log(ans ** 2);
