window.onload=function()
{
  canv=document.getElementById("snake");
  pen=canv.getContext("2d");
  dat=document.addEventListener("keydown",keyPush);
  setInterval(game,1000/10);
}

player_x=10;player_y=10;
apple_x=15;apple_y=15;
gridSize=20;tileCount=20;
y_speed=0;x_speed=0;
trail=[];
isStart=false;
tail=5;lives=10;points=0;

function game()
{
  player_x+=x_speed;
  player_y+=y_speed;
  pen.fillStyle="black";
  pen.fillRect(0,0,canv.width,canv.height);
  
  for(var i=0;i< trail.length;i++)
  {
    pen.fillStyle="lime";
    pen.fillRect(trail[i].x*gridSize,trail[i].y*gridSize,gridSize,gridSize);
    pen.lineWidth=2;
    pen.strokeStyle="black";
    pen.strokeRect(trail[i].x*gridSize,trail[i].y*gridSize,gridSize,gridSize);
    if(trail[i].x==player_x&&trail[i].y==player_y &&isStart===true)
    {lives-=1;}
    if (apple_x==player_x&&apple_y==player_y){
      tail++;
      points++;
      apple_x=Math.floor(Math.random()*tileCount);
      apple_y=Math.floor(Math.random()*tileCount);
    }
    
    pen.fillStyle="red";
    pen.fillRect(apple_x*gridSize,apple_y*gridSize,gridSize,gridSize);
    pen.strokeStyle="black";
    pen.strokeRect(apple_x*gridSize,apple_y*gridSize,gridSize,gridSize);
    
    pen.font=50+"px Arial";
    pen.textBaseline="middle";
    pen.textAlign="center";
    pen.fillStyle="white";
    pen.fillText(lives,25,25);
    pen.font=30+"px Arial";
    pen.fillText(points,20,375);
    if(lives<=0||x_speed==0&&y_speed==0){
      pen.fillText("GAME OVER",canv.height/2,canv.width/2);
      x_speed=0;
      y_speed=0;
    }
  }

  trail.push({x:player_x,y:player_y});
  while(trail.length>tail)
  {trail.shift();
  }

  if(player_x<0){player_x=tileCount-1;lives-=1;}
  if(player_x>tileCount-1){player_x=0;lives-=1;}
  if(player_y<0){player_y=tileCount-1;lives-=1;}
  if(player_y>tileCount-1){player_y=0;lives-=1;}

  pen.fillStyle="red";
  pen.fillRect(apple_x*gridSize,apple_y*gridSize,gridSize,gridSize);
}
function keyPush(evt)
{
  switch(evt.keyCode)
  {
    case 37:
    isStart=true;
    x_speed=-1;
    y_speed=0;
      break;
    case 38:
    isStart=true;
    x_speed=0;
    y_speed=-1;
      break;
    case 39:
    isStart=true;
    x_speed=1;
    y_speed=0;
      break;
    case 40:
    isStart=true;
    x_speed=0;
    y_speed=1;
      break;
  }
}
