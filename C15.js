var flips=prompt("How many times do you want to flip a coin?");
var heads=0;
var tails=0;
for(i=0;i<flips;i++){
    var num=Math.floor(Math.random()*2);
    if(num==1){
        heads+=1;
    }else{
        tails+=1;
    }
}
console.log("Total flips: "+flips);
console.log("=============");
console.log("Heads: "+heads);
console.log("Tails: "+tails);
