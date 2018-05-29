function countCharacter(str, char) {
    // your code here
    similar=0;
    for(i=0;i<(str.length);i++){
        if(str.charAt(i)==char){
            similar+=1;
        }
    }
    return(similar);
}
countCharacter("I am a hacker","a");
