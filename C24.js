function flipPairs(input){
    words=input.split("");
    n=0;
    var newList=[];
    for(var i in words){
        n+=1;
    }
    for(i=0;i<n;i++){
        if(i%2===0){
            newList.push(words[i+1]);
        }else{
            newList.push(words[i-1]);
        }
    }
    newList=newList.join("");
    return(newList);
}
flipPairs('check out how interesting this problem is, it\'s insanely interesting!');
