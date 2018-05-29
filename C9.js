function convertScoreToGradeWithPlusAndMinus(score) {
// your code here
    if(score<0){
        return("INVALID SCORE");
    }
    if(score<=59){
        return("F");
    }
    if(59<score && score<=69){
        if(69>=score<=68){
            return("D+");
        }
        if(60>=score && score<=62);{
            return("D-");
        }
        if(67>=score && score<=63);{
            return("D");
        }
    }
    if(69<score && score<=79){
        if(79>=score && score>=78){
            return("C+");
        }
        if(70>=score && score<=72);{
            return("C-");
        }
        if(77>=score && score<=73);{
            return("C");
        }
    }
    if(79<score && score<=89){
        if(89>=score && score>=88){
            return("B+");
        }
        if(80>=score && score<=82);{
            return("B-");
        }
        if(87>=score && score<=83);{
            return("B");
        }
    }
    if(89<score && score<=99){
        if(100>=score && score<=98){
            return("A+");
        }
        if(90>=score && score<=92);{
            return("A-");
        }
        if(97>=score && score<=93);{
            return("A");
        }
    }
    if(score>100){
        retutn("INVALID SCORE");
    }
}
convertScoreToGradeWithPlusAndMinus(77);
