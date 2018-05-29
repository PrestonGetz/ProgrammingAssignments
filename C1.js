function cToF(celsius) {
var fahrenheit=(celsius*1.8)+32;
console.log(celsius+"\xB0"+"c is "+fahrenheit+"\xB0"+"F.");
}

function fToC(fahrenheit) {
var celsius=(5/9)*(fahrenheit-32);
console.log(fahrenheit+"\xB0"+"F is "+celsius+"\xB0"+"C.");
}

cToF(60);
fToC(45);
