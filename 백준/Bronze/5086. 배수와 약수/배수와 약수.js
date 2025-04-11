const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim().split(/\r?\n/);

let ans = "";
for (let i = 0; i < fileData.length; i++) {
  const [num1, num2] = fileData[i].split(" ");

  if (num1 == 0 && num2 == 0) {
    break;
  }

  if (num2 % num1 == 0) {
    ans = "factor";
  } else if (num1 % num2 == 0) {
    ans = "multiple";
  } else {
    ans = "neither";
  }

  console.log(ans);
}
