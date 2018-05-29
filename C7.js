function computeSumBetween(num1, num2) {
    // your code here
    if(num1>num2){
        return(0);
    }else{
        output=0;
        for (var i=num1;i<num2;i++){
            output+=i;
        }
        return(output);
    }
}
computeSumBetween(2,5);
