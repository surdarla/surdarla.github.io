const problem_num = "";
const path = `${__dirname}\\txt\\${problem_num}.txt`;
// const path = "/dev/stdin";

const input = require("fs").readFileSync(path, 'utf8').toString().trim().split('\n');
let currentLine = 0;

function readLine() {
    return input[currentLine++].split(' ').map(Number);
}
