/* /*
  Challenge 1


let a = 10;
let b = "20";
let c = 80;

console.log(++a + +b++ + +c++ - +a++);
console.log(++a + -b + +c++ - -a++ + +a);
console.log(--c + +b + --a * +b++ - +b * a + --a - +true);

/*
  [++a] [+] [+b++] [+] [+c++] [-] [+a++]

  [++a]
  - Value: 11
  - Explain: pre increment.
  [+]
  - Explain: Addition.

  [+b++]
  - Value: 20
  - Explain: post increment.
  [+]
  - Explain: Addition.

  [+c++]
  - Value: 80
  - Explain: post increment.
  [-]
  - Explain: Subtraction.

  [+a++]
  - Value: 11
  - Explain: post increment.
*/

/*
  [++a] [+] [-b] [+] [+c++] [-] [-a++] [+] [+a]

  [++a]
  - Value: 13
  - Explain: pre increment.
  [+]
  - Explain: Addition.

  [-b]
  - Value: -21
  - Explain: post increment.
  [+]
  - Explain: Addition.

  [+c++]
  - Value: 81
  - Explain: post increment.
  [-]
  - Explain: Subtraction.

  [-a++]
  - Value: -13
  - Explain: post increment.
  [+]
  - Explain: Addition.

  [+a]
  - Value: 13
  - Explain: plus unary.
*/

/*
  [--c] [+] [+b] [+] [--a] [*] [+b++] [-] [+b] [*] [a] [+] [--a] [-] [+true]

  [--c]
  - Value: 81
  - Explain: pre decrement.
  [+]
  - Explain: Addition.

  [+b]
  - Value: 21
  - Explain: unary plus.
  [+]
  - Explain: Addition.

  [--a]
  - Value: 13
  - Explain: pre decrement.
  [*]
  - Explain: Multiplication.

  [+b++]
  - Value: 21
  - Explain: post increment.
  [-]
  - Explain: Subtraction.

  [+b]
  - Value: 22
  - Explain: plus unary.
  [*]
  - Explain: Multiplication.

  [a]
  - Value: 13
  - Explain: none.
  [+]
  - Explain: Addition.

  [--a]
  - Value: 12
  - Explain: pre decrement.
  [-]
  - Explain: Subtraction.

  [+true]
  - Value: 1
  - Explain: plus unary.
*/


/*
  Challenge 2




// Only Use Variables Value
// Do Not Use Variable Twice

console.log(+e % f * -d / +g); // 2000
console.log(); // 173 */

let d = "-100";
let e = "20";
let f = 30;
let g = true;

console.log(-d * (+e / +g) * f)