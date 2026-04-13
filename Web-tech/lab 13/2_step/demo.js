let x = 50;
let y = 10;

console.log("Сума x + y =", x + y);

let d = x * y;
console.log("d = x * y =", d);

let firstName = "Назар", lastName = "Гучко", age = 17;

d = d / y;
x = x - d;
age = age + x;

console.log(firstName + " " + lastName + " " + age);

if (age >= 18) {
    console.log("студент повнолітній");
} else {
    console.log("студент неповнолітній");
}

age = "18";
console.log(age == 18);
console.log(age === 18);

let N = 2;

for (let i = 1; i <= 10 * N + 3; i++) {
    if (i % 2 !== 0) {
        console.log(i);
    }
}