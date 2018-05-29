function noDuplicates(phrase){
    var words=phrase.split(" ");
    var list=words.sort();
    var same=false;
    n=0;
    for(var x in list){
        n+=1;
    }
    for(i=1;i<n;i++){
        if(list[i]==list[i-1]){
            return("no");
        }
    }
    return("yes");
}
noDuplicates("IN THE RAIN AND THE SNOW");
