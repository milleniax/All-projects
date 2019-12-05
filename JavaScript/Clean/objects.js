//check whether massiv is empty
function isEmpty(obj) {
    for (feature in obj) {
        return "false";
    }
    return "true";
}
let schedule = {
    name: "john"
};
console.log(isEmpty(schedule));

//sum of object key values 
function sum(obj){
    let sum = 0;
    for (key in obj){
        sum += obj[key];
    }
    return sum;
}
let salaries = {
    John: 100,
    Ann: 160,
    Pete: 130
  }
  console.log(sum(salaries));

//calculator

  let calculator = {
      a:null,
      b:null,
      read()
      {
          this.a = +prompt("Enter first number");
          this.b = +prompt("Enter second number");
      },
      sum(){
          return this.a + this.b; 
      },
      mul(){
          return this.a*this.b;
      }
  }
calculator.read();
alert(calculator.mul());
alert(calculator.sum());

//prototype-inheritance

let head = {
    glasses: 1,
  };
  
  let table = {
    pen: 3,
    __proto__: head
  };
  
  let bed = {
    sheet: 1,
    pillow: 2,
    __proto__: table 
  };
  
  let pockets = {
    money: 2000,
    __proto__: bed
  };

console.log(pockets.sheet)


function Rabbit(name) {
    this.name = name;
}
let rabbit = new Rabbit("cock");
console.log(typeof rabbit);