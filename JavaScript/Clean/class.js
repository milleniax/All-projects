class FormatError extends Error{
    constructor(message){
        super(message);
        this.name = "FormatError";
        this.stack = "stack";
    }
}
let err = new FormatError("Donna work");
console.log(err.name);
console.log(err.message);
console.log(err.stack);

function func(message){
    throw new FormatError("Donna work");
    alert(message);
}

try{
    alert("helo");
}
catch(e){
    console.log(e.message);
}
try{
    func("helo");
}
catch(e){
    console.log(e.message);
}