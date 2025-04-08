const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

let firstLine = inputData[0].trim().split(" ");
let N = Number(firstLine[0]);
let M = Number(firstLine[1]);

let arr1 = [];
let arr2 = [];
let data;

for (let i = 1; i <= N; i++) {
  data = inputData[i].trim().split(" ");
  arr1.push(data);
}

for (let i = N + 1; i < inputData.length; i++) {
  data = inputData[i].trim().split(" ");
  arr2.push(data);
}

for (let i = 0; i < N; i++) {
  data = [];
  for (let j = 0; j < M; j++) {
    data.push(Number(arr1[i][j]) + Number(arr2[i][j]));
  }
  console.log(data.join(" "));
}
