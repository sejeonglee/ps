const fs = require("fs");
// const filePath = "/dev/stdin";
const filePath = "./input.txt";
const input = fs.readFileSync(filePath).toString();

function process(sentence) {
  const characters = ["U", "C", "P", "C"];
  for (const c of characters.values()) {
    const n = sentence.indexOf(c);
    if (n === -1) {
      return "I hate UCPC";
    }
    sentence = sentence.substring(n + 1);
  }
  return "I love UCPC";
}
console.log(process(input));
