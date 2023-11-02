const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

class Student {
    constructor(name, k, e, m) {
        this.name = name;
        this.k = k;
        this.e = e;
        this.m = m;
    }
}

const students = [];
let n = 0;

// 먼저 학생 수 n을 입력받습니다.
rl.question('n: ', (num) => {
    n = parseInt(num);
    let count = 0;

    // 학생 정보를 입력받는 함수
    function recursive() {
        rl.question('student: ', (input) => {
            const [name, k, e, m] = input.split(' ');
            students.push(new Student(name, parseInt(k), parseInt(e), parseInt(m)));
            count++;

            if (count < n) {
                recursive(); // 다음 학생 정보 입력을 받음
            } else {
                sortAndLog();
            }
        });
    }

    // 첫 번째 학생 정보 입력을 시작
    recursive();
});

function sortAndLog() {
    // 학생들을 정렬
    students.sort((a, b) => {
        if (a.k !== b.k) {
            return b.k - a.k;
        } else if (a.e !== b.e) {
            return a.e - b.e;
        } else if (a.m !== b.m) {
            return b.m - a.m;
        } else {
            return a.name.localeCompare(b.name);
        }
    });

    // 정렬된 학생 정보를 출력
    students.forEach(student => console.log(student.name));
    rl.close();
}
