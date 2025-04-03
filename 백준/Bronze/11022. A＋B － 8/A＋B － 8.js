const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

const t = parseInt(inputData[0]);

for (let i = 1; i <= t; i++) {
  const data = inputData[i].trim().split(" ");
  console.log(
    `Case #${i}: ${data[0]} + ${data[1]} = ${
      parseInt(data[0]) + parseInt(data[1])
    }`
  );
}