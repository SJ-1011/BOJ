const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim().split(" ");

const A = parseInt(fileData[0]);
const B = parseInt(fileData[1]);
const V = parseInt(fileData[2]);

const day = Math.ceil((V - B) / (A - B));
console.log(day);
