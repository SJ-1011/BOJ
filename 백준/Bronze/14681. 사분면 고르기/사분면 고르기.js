const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

let x = inputData[0];
let y = inputData[1];

if (x > 0 && y > 0) {
  console.log(1);
} else if (x < 0 && y > 0) {
  console.log(2);
} else if (x < 0 && y < 0) {
  console.log(3);
} else {
  console.log(4);
}