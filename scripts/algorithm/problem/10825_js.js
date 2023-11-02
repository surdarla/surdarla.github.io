const path = require('path');
const fs = require('fs');
const problemNum = 10825;
const filePath = path.join(__dirname, 'txt', `${problemNum}.txt`);
const fileContent = fs.readFileSync(filePath, 'utf8');
const lines = fileContent.split('\n');

const n = lines[0];

class Student {
    constructor(name, korean, english, math) {
        this.name = name;
        this.korean = korean;
        this.english = english;
        this.math = math;
    }
};

let students = [];
for (let i = 1; i < n; i++) {
    const [name, korean, english, math] = lines[i].replace('\r','').split(' ');
    students.push(new Student(name, parseInt(korean), parseInt(english), parseInt(math)));
};

function sortStudents() {
    const sortedData = students.sort((a, b) => {
        if (a.korean !== b.korean) {
            return b.korean - a.korean;
        }
        if (a.english !== b.english) {
            return a.english - b.english;
        }
        if (a.math !== b.math) {
            return b.math - a.math;
        }
        return a.name.localeCompare(b.name);
    })
}

sortStudents();
students.forEach(student => {
    console.log(student.name);
})
