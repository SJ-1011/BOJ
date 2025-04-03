const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

const t = parseInt(inputData[0]);
let sum = "";

for (let i = 1; i <= t; i++) {
  const data = inputData[i].trim().split(" ");
  sum += (parseInt(data[0]) + parseInt(data[1])) + "\n";
}

console.log(sum);