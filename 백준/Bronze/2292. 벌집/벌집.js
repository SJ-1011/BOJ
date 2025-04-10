const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim();

const N = Number(fileData);

// 층 당 1 + 6n개의 벌집이 있음
// 총 1 + 6 * (n-1)*n/2

let layer = 1;
let maxNum = 1;

while (N > maxNum) {
  maxNum += 6 * layer;
  layer++;
}

console.log(layer);
