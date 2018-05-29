function getLongestWordOfMixedElements(arr) {
    // your code here
    var longest = "";
    for(var i=0;i<arr.length;i++){
        if(arr[i].length>longest.length){
            longest=arr[i];
        }
    }
    return(longest);
}
getLongestWordOfMixedElements(["one","two","three"]);
