const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();

let problem = inputData.toUpperCase();
let char = [];
let num = [];

for (let i = 0; i < problem.length; i++) {
  if (!char.includes(problem[i])) {
    char.push(problem[i]);
    num.push(1);
  } else {
    num[char.indexOf(problem[i])] += 1;
  }
}

let ans;
let max = Math.max(...num);

ans = char[num.indexOf(max)];
let count = 0;

for (let i = 0; i < num.length; i++) {
  if (max == num[i]) {
    count++;
  }
}

if (count > 1) {
  ans = "?";
}
console.log(ans);
