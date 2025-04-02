const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(" ");

let lines = parseInt(inputData);

ans = "";
for (let i = 1; i <= lines; i++) {
  for (let j = 1; j <= lines - i; j++) {
    ans += " ";
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    ans += "*";
  }
  console.log(ans);
  ans = "";
}
ans = "";
for (let i = lines - 1; i >= 1; i--) {
  for (let j = 1; j <= lines - i; j++) {
    ans += " ";
  }
  for (let k = 1; k <= 2 * i - 1; k++) {
    ans += "*";
  }
  console.log(ans);
  ans = "";
}
