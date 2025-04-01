const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split(" ");

let num1 = parseInt(inputData[0]);
let num2 = parseInt(inputData[1]);
let num3 = parseInt(inputData[2]);

//10,000원+(같은 눈)×1,000원
//1,000원+(같은 눈)×100원
//(그 중 가장 큰 눈)×100원

if (num1 == num2 && num1 == num3) {
  console.log(`${10000 + num1 * 1000}`);
} else if (num1 == num2 || num3 == num1) {
  console.log(`${1000 + num1 * 100}`);
} else if (num2 == num3) {
  console.log(`${1000 + num2 * 100}`);
} else {
  console.log(`${Math.max(num1, num2, num3) * 100}`);
}