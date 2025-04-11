const fs = require("fs");
const [N, K] = fs.readFileSync(0).toString().trim().split(" ");
let cnt = 0;
let flag = false;

for (let i = 1; i <= N; i++) {
  if (N % i == 0) {
    cnt++;
  }
  if (cnt >= K) {
    flag = true;
    console.log(i);
    break;
  }
}

if (!flag) {
  console.log(0);
}
