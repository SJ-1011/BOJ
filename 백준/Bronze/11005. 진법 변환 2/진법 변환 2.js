const fs = require("fs");
const fileData = fs.readFileSync(0).toString().trim().split(" ");
const N = parseInt(fileData[0]); // 바꿀 10진수
const B = Number(fileData[1]); // 진법 ex.16진수

let tmp = N;
let rest;
let arr = [];
let ans = "";

// 나머지, 마지막으로 남은 몫 계산 후 arr에 저장
while (tmp >= B) {
  rest = tmp % B;
  tmp = parseInt(tmp / B);
  arr.push(rest);
}
arr.push(tmp);

// 9보다 큰 수는 A~Z로 바꾸고 역순으로 출력
for (let i = arr.length - 1; i >= 0; i--) {
  if (arr[i] >= 10) {
    arr[i] = String.fromCharCode(arr[i] + 55);
  }
  ans += arr[i];
}

console.log(ans);
