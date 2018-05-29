function acronymMaker(str){
    words=str.split(" ");
    letters=[];
    for(var i in words){
        firstLetter=words[i].split("");
        letters.push(firstLetter[0]);
    }
    return(letters.toString());
}
acronymMaker("Portable Network Graphics");
