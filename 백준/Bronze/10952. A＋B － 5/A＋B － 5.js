const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

for (let i = 0; i < inputData.length - 1; i++) {
  const data = inputData[i].trim().split(" ");
  console.log(parseInt(data[0]) + parseInt(data[1]));
}