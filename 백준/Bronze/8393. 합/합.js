const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();

let sum = 0;
for (let i = 1; i <= parseInt(inputData); i++) {
  sum += i;
}

console.log(sum);