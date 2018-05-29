function calculateBillTotal(preTaxAndTipAmount) {
    // your code here
    var tax=(preTaxAndTipAmount*0.095);
    var tip=(preTaxAndTipAmount*0.15);
    var bill=preTaxAndTipAmount+tip+tax;
    return(bill);
}
calculateBillTotal(20);
