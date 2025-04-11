const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split(/\r?\n/);
let sum;
let num;
let list;
for (let i = 0; i < input.length; i++) {
  num = input[i];
  sum = 0;
  list = [];

  if (num == -1) {
    break;
  }

  for (let j = 1; j < num; j++) {
    if (num % j == 0) {
      sum += j;
      list.push(j, "+");
    }
  }
  if (num == sum) {
    list.pop();
    console.log(`${num} = ${list.join(" ")}`);
  } else {
    console.log(`${num} is NOT perfect.`);
  }
}
