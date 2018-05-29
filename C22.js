function checkCar() {
    var text;
    var favCar=prompt("input a car");
    switch(favCar){
        // add code here
        case "BMW":
            text="German car";
            break;
        case "Ford":
            text="American car";
            break;
        case "Peugeot":
            text="French car";
            break;
    }
    return(text);
}
checkCar();
