function loneSum(a,b,c){
    total=0;
    if(a==b){
        if(a==c){
            return(0);
        }else{
            return(c);
        }
    }else if(a==c){
        return(b);
    }else if(b==c){
        return(a);
    }else{
        return(a+b+c);
    }
}
loneSum(1,2,3);
