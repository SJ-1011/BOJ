const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

for (let i = 0; i < inputData.length; i++) {
  console.log(inputData[i]);
}
