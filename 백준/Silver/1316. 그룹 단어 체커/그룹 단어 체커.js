const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

let N = parseInt(inputData[0]);
let str_arr = [];

let bool = true;
let ans = 0;

for (let i = 1; i <= N; i++) {
  let data = inputData[i];
  for (let j = 0; j < data.length; j++) {
    if (!str_arr.includes(data[j])) {
      str_arr.push(data[j]);
    } else {
      if (data[j] != data[j - 1]) {
        bool = false;
        break;
      }
    }
  }
  str_arr = [];

  if (bool) {
    ans += 1;
  }

  bool = true;
}

console.log(ans);
