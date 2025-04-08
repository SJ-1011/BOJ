const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim().split("\n");

let sum = 0;
let classes = 0;

for (let i = 0; i < inputData.length; i++) {
  let data = inputData[i].trim().split(" ");
  let score = 0;
  let subject = Number(data[1]);

  if (data[2] != "P") {
    switch (data[2]) {
      case "A+":
        score = 4.5;
        break;
      case "A0":
        score = 4.0;
        break;
      case "B+":
        score = 3.5;
        break;
      case "B0":
        score = 3.0;
        break;
      case "C+":
        score = 2.5;
        break;
      case "C0":
        score = 2.0;
        break;
      case "D+":
        score = 1.5;
        break;
      case "D0":
        score = 1.0;
        break;
      case "F":
        score = 0;
        break;
    }
    sum += subject * score;
    classes += subject;
  }
}

console.log(sum / classes);
