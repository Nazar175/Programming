let products = [
    { name: "Samsung J5 2017", screen: 5.2, price: 5400, weight: 160 },
    { name: "iPhone X", screen: 5.8, price: 25000, weight: 170 },
    { name: "Xiaomi Mi 4", screen: 5.5, price: 4999, weight: 150 },
    { name: "Nokia 3310 2018", screen: 2.4, price: 999, weight: 60 },
    { name: "iPhone 7", screen: 4.7, price: 9999, weight: 140 }
];

let minPrice = 2000;
let maxPrice = 10000;

let result = [];

for (let i = 0; i < products.length; i++) {
    if (products[i].price >= minPrice && products[i].price <= maxPrice) {
        result.push(products[i]);
    }
}

console.log("Результат:");
console.log(result);

let trips = [
    { city: "Київ", duration: 2, price: 2000, food: false, guide: true },
    { city: "Харків", duration: 1, price: 3000, food: true, guide: false },
    { city: "Одеса", duration: 2, price: 4500, food: true, guide: true },
    { city: "Дніпро", duration: 1, price: 5500, food: false, guide: true },
    { city: "Полтава", duration: 1, price: 3000, food: false, guide: false },
    { city: "Львів", duration: 2, price: 6000, food: true, guide: true }
];

let oneDayNoFood = [];

for (let trip of trips) {
    if (trip.duration === 1 && trip.food === false) {
        oneDayNoFood.push(trip);
    }
}

console.log("Одноденні подорожі без харчування:");
console.log(oneDayNoFood);

let cheapTrips = [];

for (let trip of trips) {
    if (trip.price <= 3000) {
        cheapTrips.push(trip);
    }
}

console.log("Подорожі до 3000 грн:");
console.log(cheapTrips);

function sum(x, y, z) {
    return x + y + z;
}

console.log("Результат sum:");
console.log(10 + sum(2, 3, 4) + sum(1, 1, 1));

function sayHello(name) {
    console.log("Привіт, " + name + "!");
}

sayHello("Назар");

function printSomeNumber() {
    console.log(42);
}

printSomeNumber();