var a=0;
var b=0;
for(i=0;i<11;i++){
    console.log(a+" TIMES TABLE");
    for(x=0;x<11;x++){
        console.log(a+" x "+b+" = "+(a*b));
        b+=1;
    }
    b=0;a+=1;
}
