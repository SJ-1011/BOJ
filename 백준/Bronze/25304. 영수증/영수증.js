const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

const totalPrice = parseInt(inputData[0]);
const T = parseInt(inputData[1]);

let sum = 0;
for (let i = 2; i < T + 2; i++) {
  const data = inputData[i].trim().split(" ");
  sum += parseInt(data[0]) * parseInt(data[1]);
}

if (sum == totalPrice) {
  console.log("Yes");
} else {
  console.log("No");
}