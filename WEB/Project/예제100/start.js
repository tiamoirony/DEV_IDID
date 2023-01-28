// console.log('hello world!');
// console.log('hello world!');

// let s = 0;

// for (let i=1; i<=100; i++){
//     s += i;
// }

// console.log(s)


// const Wizard = class Wizard {
//     constructor (health, mana, armor){
//         this.health = health;
//         this.mana = mana;
//         this.armor = armor;

//     }
//     attack(){
//         console.log('파이어볼');
//     }
// }

// const x = new Wizard(545, 210, 10);
// console.log(x.health, x.mana, x.armor);
// x.attack();

// // **출력**
// // 545 210 10
// // 파이어볼

// const planets = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성'];

// const n = prompt('몇 번째 행성인가요?');

// console.log(planets[n-1]);

// const n = prompt('숫자를 입력하세요.');


// if (n%3 == 0) { // 나머지 연산 %는 n을 3으로 나누었을때 몫이 아닌 나머지 값을 반환합니다.
//     console.log('짝');
// } else {
//     console.log(n);
// }

// const name = prompt('이름은?');
// console.log(`안녕하세요. 저는 ${name}입니다.`); 

// const n = prompt('입력하세요.');

// const reverseString = n.split('').reverse().join('');
// /*
// * split() 메서드는 문자열을 배열로 만들어 반환하고,
// * reverse() 메서드는 배열의 순서를 반전하며,
// * join() 메서드는 원소를 모두 붙여 문자열로 반환합니다.
// */
// console.log(reverseString);

// const height = prompt('키를 입력하세요.');

// if (height >= 150){
//     console.log("YES");
//   } else {

//     console.log("NO");
//   }


// const scores = prompt('세 과목의 점수를 입력하세요.').split(' ');
// let sum = 0;

// for (let i=0; i<3; i++){
//   sum += parseInt(scores[i], 10); // 십진수의 형태의 숫자로 데이터 타입을 변환합니다.
// }

// console.log(Math.floor(sum/3)); //Math.floor 메서드는 소수점 자리를 모두 버림합니다.

// const n = prompt('수를 입력하세요.').split(' ');

// const result = Math.floor(parseInt(n[0], 10) / parseInt(n[1], 10));
// const left = parseInt(n[0], 10) % parseInt(n[1], 10);

// console.log(result, left);


// var name = prompt("이름을 입력하세요.");

// console.log(name.toUpperCase());


// function circle(n) {
//     const result = n * n * 3.14;
  
//     return result;
//   }
  
//   const r = prompt("원의 반지름을 입력하세요.");
  
//   console.log(circle(r));

// const planets = {
// 	'수성' : 'Mercury',
// 	'금성' : 'Venus',
// 	'지구' : 'Earth',
// 	'화성' : 'Mars',
// 	'목성' : 'Jupiter',
// 	'토성' : 'Saturn',
// 	'천왕성' : 'Uranus',
// 	'해왕성' : 'Neptune',
// };

// const name = prompt("행성의 이름을 입력하세요.");

// console.log(planets[name]);

// const keys = prompt('이름을 입력하세요').split(' ');
// const values = prompt('점수를 입력하세요').split(' ');
// const obj = {};

// for (let i=0; i<keys.length; i++) {
//   obj[keys[i]] = parseInt(values[i]);
// }

// console.log(obj);


// function one(n) {
//     function two(value) {
//         const sq = Math.pow(value, n);
//         return sq;
//     }
//     return two;
//     }

// const a = one(2);
// const b = one(3);
// const c = one(4);

// console.log(a(10));
// console.log(b(10));
// console.log(c(10));


// var count = prompt("입력");
// var count_list = count.split("");
// var count_list = parseInt.count_list;
// console.log(count_list);
// for (let i; i < i + 1; i++) {
// if (count_list[i] < count_list[i] + 1) {
// console.log("YES");
// } else {
// console.log("no");
// }
// }

// var count = prompt("입력");
// var count_list = count.split("");
// var count_list = parseInt.count_list;

// console.log(count_list);

// for (let i; i < i + 1; i++) {
// if (count_list[i] < count_list[i] + 1) {

// console.log("YES");
// } else {
// console.log("no");
// }
// }


// while(i<height_split.length){
//     let a = height_split[i-1]
//     let b = height_split[i]

//     if(a<b){
//     result.push('yes')
//     }else{
//     break;
//     }
//     i++;
//     };
//     if(height_split.length == result.length+1){
//     console.log('YES')
//     }else{
//     console.log('NO')
//     };


//     let tall = prompt("키를 입력하세요").split(" ");
//     let tall_r = "";
    
//     tall_r = tall
//     .sort(function (a, b) {
//     return a - b;
//     })
//     .join(" ");
//     // console.log(tall_r);
    
//     if (tall == tall_r) {
//     console.log("Yes");
//     } else {
//     console.log("No");
//     }


//     const a = prompt().split(" ");
//     b = a.reduce((acc, cur) => {
//     if (acc.hasOwnProperty(cur)) {
//     acc[cur]++;
//     } else {
//     acc[cur] = 1;
//     }
//     return acc;
//     }, {});

//     c = Object.values(b).sort((x, y) => y - x);
//     function getKeyByValue(object, value) {
//     return Object.keys(object).find((key) => object[key] === value);
//     }
//     let key = getKeyByValue(b, c[0]);
//     console.log(key,c[0]);


// document.querySelector('button.num37').addEventListener('click',()=>{
//     let vote = document.querySelector('input.num37').value;
//     let list = vote.split(' ')
//     let students = new Set(list);
//     let stu_list = [...students];
//     let stu_dict = {};
    
//     for (i = 0; i < stu_list.length; i++) {
//     stu_dict[stu_list[i]] = list.filter((str) => str == stu_list[i]).length;
//     };
//     max = Math.max(...Object.values(stu_dict));
//     key_list = Object.keys(stu_dict);

//     for (j = 0; j < key_list.length; j++) {
//     if (stu_dict[key_list[j]] == max) {
//     console.log(Object.keys(stu_dict)[j]+'(이)가 총 '+stu_dict[Object.keys(stu_dict)[j]]+ '표로 반장이 되었습니다.');
//     };
//     };
//     });


//     var totals =
//     // (parseInt(score[0]) + parseInt(score[1]) + parseInt(score[2])) / 3;
//     // var totals_ans = Math.floor(totals);
//     // document.write(totals_ans);


//     var a = prompt().split(" ");
//     var s = 0;
//     a.forEach((i) => {
//     s += Number(i);
//     });
//     console.log(Math.floor(s / 3));


    // ceil
    // while(num !=1){
    // if(num%2==0){
    // result.unshift(num%2)
    // num = parseInt(num/2)
    // }else{
    // result.unshift(num%2)
    // num = parseInt(num/2)
    // }
    // }
    // result.unshift(1)
    // for(i=0;i<result.length;i++){
    // binary+=result[i]
    // }

// ceil
// while(num !=1){
// if(num%2==0){
// result.unshift(num%2)
// num = parseInt(num/2)
// }else{
// result.unshift(num%2)
// num = parseInt(num/2)
// }
// }
// result.unshift(1)
// for(i=0;i<result.length;i++){
// binary+=result[i]
// }


// let result = [];
// let binary = ''
// while(num !=1){
// if(num%2==0){
// result.unshift(num%2)
// num = parseInt(num/2)
// }else{
// result.unshift(num%2)
// num = parseInt(num/2)
// }
// }
// result.unshift(1)
// for(i=0;i<result.length;i++){
// binary+=result[i]
// }


// console.log(Number(prompt()).toString(2))

// 50 

// let sec = (b.getTime()/1000-a.getTime()/1000)/86400
// let sec = (b.getTime()-a.getTime())/86400000

// let a= new Date(2020,1,1);
// let b= new Date(2020,date[0],date[1]);

// //  41

// for(i=1;i<=number;i++){
//     if(number%i==0){
//     result.push(i)
//     }
//     }
//     if(result.length==2){
//     answer = 'YES'
//     }else{
//     answer = 'NO'
//     }

