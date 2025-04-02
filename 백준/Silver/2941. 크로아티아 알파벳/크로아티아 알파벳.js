const fs = require("fs");
const inputData = fs.readFileSync(0).toString().trim();

let count = 0;

for (let i = 0; i < inputData.length; i++) {
  if (inputData[i] == "c") {
    if (inputData[i + 1] && inputData[i + 1] == "=") {
      continue;
    } else if (inputData[i + 1] && inputData[i + 1] == "-") {
      continue;
    }
  } else if (inputData[i] == "d") {
    if (
      inputData[i + 2] &&
      inputData[i + 1] == "z" &&
      inputData[i + 2] == "="
    ) {
      continue;
    } else if (inputData[i + 1] && inputData[i + 1] == "-") {
      continue;
    }
  } else if (inputData[i] == "l") {
    if (inputData[i + 1] && inputData[i + 1] == "j") {
      continue;
    }
  } else if (inputData[i] == "n") {
    if (inputData[i + 1] && inputData[i + 1] == "j") {
      continue;
    }
  } else if (inputData[i] == "s") {
    if (inputData[i + 1] && inputData[i + 1] == "=") {
      continue;
    }
  } else if (inputData[i] == "z") {
    if (inputData[i + 1] && inputData[i + 1] == "=") {
      continue;
    }
  }
  count++;
}

console.log(count);
