<!DOCTYPE html>
<html>
<body>
<canvas id="clock" width="500" height="500" style="background-color:#1f4c04"></canvas>
<script>

var canvas=document.getElementById("clock");
var pen=canvas.getContext("2d");
var radius=canvas.height/2;
pen.translate(radius,radius);
radius = radius * 0.90;

setInterval(drawClock,1000);

function drawClock(){
  drawFace(pen,radius);
  drawNumbers(pen,radius);
  drawTime(pen,radius);
}

function drawFace(pen,radius){
  pen.beginPath();
  pen.arc(0,0,radius,0,2*Math.PI);
  pen.fillStyle="#7aef97";
  pen.fill();
  
  pen.beginPath();
  pen.arc(0,0,radius,0,2*Math.PI);
  pen.strokeStyle="green";
  pen.lineWidth=radius*0.10;
  pen.stroke();
  
  pen.beginPath();
  pen.arc(0,0,radius*0.05,0,2*Math.PI);
  pen.fillStyle="black"
  pen.fill();
  
}

function drawNumbers(pen,radius){
  var ang=30*Math.PI/180;
  pen.font=radius*0.15+"px Calibri";
  pen.textBaseline="middle";
  pen.textAlign="center";
  pen.fillStyle="#1f4c04";
  
  for(i=1;i<13;i++){
    pen.rotate(ang);
    pen.translate(0,-radius*.85);
    pen.rotate(-ang);
    pen.fillText(i.toString(),0,0);
    pen.rotate(ang);
    pen.translate(0, radius*.85);
    pen.rotate(-ang);
    ang+=30*Math.PI/180
  }
}

function drawTime(pen,radius) {
  var now=new Date();
  var hour=now.getHours();
  var minute=now.getMinutes();
  var second=now.getSeconds();
  
  hour=hour%12;
  hour=(hour*Math.PI/6) + 
  (minute*Math.PI/(6*60)) +
  (second*Math.PI/(6*60*60));
  drawHand(pen,hour,radius*0.5,radius*0.07);
  
  minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
  drawHand(pen,minute,radius*0.75,radius*0.06);
  
  second=(second*Math.PI/30);
  drawHand(pen,second,radius*0.8,radius*0.02);
  
}

function drawHand(pen,pos,length,width){
  pen.beginPath();
  pen.lineWidth=width;
  pen.lineCap="round";
  pen.moveTo(0,0);
  pen.rotate(pos);
  pen.lineTo(0,-length);
  pen.stroke();
  pen.rotate(-pos);
}

</script>

</body>
</html>
