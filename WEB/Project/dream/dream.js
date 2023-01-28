// 1. Use strict
// added in ES 5
// use this for Valina Javascript.
'use strict';


// 2. Variable
// let (added in ES6)




let name = 'ellit';
console.log(name);

name = 'hello';
console.log(name);



// 4. Variable types
// primitive , single item : number, string, boolean, unll, undefiedn, symbol
// object, box container
// function, first-class function 



const count = 7;
const size = 17.1;

console.log(`value: ${count}, type: ${typeof count}`);
console.log(`value: ${size}, type: ${typeof size}`);


// number 

const infinity = 1 / 0;
const negativeInfinity = -1 / 0 ;
const nAn = 'not a number' / 2;

console.log(infinity);
console.log(negativeInfinity);
console.log(nAn);


// bigInt
const bigInt = 12312312312131231n;
console.log(`value: ${bigInt}, type: ${typeof bigInt}`);


// string 

const char = 'c';
const brendan = 'brendan';
const greeting = 'hello' + brendan;

console.log(`value: ${greeting}, type: ${typeof greeting}`);

const helloBob = `hi ${brendan}!`;
console.log(`value: ${helloBob}, type: ${typeof helloBob}`);

// boolean
// false:0, null, undefined, NaN, ''
// true: any other value 

const canRead = true;
const test = 3 < 1;
console.log(`value: ${canRead}, type: ${typeof canRead}`);
console.log(`value: ${test}, type: ${typeof test}`);

// null
let nothing = null;
console.log(`value: ${nothing}, type: ${typeof nothing}`);

//undefined
let x;
console.log(`value: ${x}, type: ${typeof x}`); 

//symbol, create unique identifiers for objects
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2);
const ssymbol1 = Symbol.for('id');
const ssymbol2 = Symbol.for('id');