const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(" ");

console.log(
  1 - parseInt(inputData[0]),
  1 - parseInt(inputData[1]),
  2 - parseInt(inputData[2]),
  2 - parseInt(inputData[3]),
  2 - parseInt(inputData[4]),
  8 - parseInt(inputData[5])
);
