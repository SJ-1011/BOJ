const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();
let t = parseInt(inputData);
let str = "";

for (let i = 0; i < t / 4; i++) {
  str += "long ";
}

str += "int";
console.log(str);