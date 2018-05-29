function owassoRams(n){
    a=[];
    for(i=1;i<n+1;i++){
        if(i%3===0){
            if(i%5===0){
                a.push("OwassoRams");
            }else{
                a.push("Owasso");
            }
        }else if(i%5===0){
            a.push("Rams");
        }else{
            a.push(i);
        }
    }
    return(a);
}
owassoRams(100);
