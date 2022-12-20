// Numero random 1-6
let randomNumber1 = Math.floor(Math.random()*6) + 1;

let randomNumber2 = Math.floor(Math.random()*6) + 1;

let randomDice1 = `images/dice${randomNumber1}.png`;

let randomDice2 = `images/dice${randomNumber2}.png`;

//Seleccion de dado 1

let dice1 = document.querySelectorAll('img')[0];

dice1.setAttribute('src', randomDice1);

//Seleccion de dado 2

let dice2 = document.querySelectorAll('img')[1];

dice2.setAttribute('src', randomDice2);