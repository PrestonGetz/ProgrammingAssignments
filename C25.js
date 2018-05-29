function triangleOrNot(a,b,c){
    var a2b2=(Math.pow(a,2))+(Math.pow(b,2));
    var c2=(Math.pow(c,2));
    var rightTriangle="false";
    if(a2b2==c2){
        rightTriangle="true";
    }
    return(rightTriangle);
}
triangleOrNot(5,6,7);
