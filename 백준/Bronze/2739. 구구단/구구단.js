const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();

for (let i = 1; i <= 9; i++) {
  console.log(`${inputData} * ${i} = ${parseInt(inputData) * i}`);
}