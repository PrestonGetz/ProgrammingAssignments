window.onload=function(){
    canvas=document.createElement("canvas");
    canvas.width=window.innerWidth-20;
    canvas.height=window.innerHeight-20;
    document.body.appendChild(canvas);
    pen=canvas.getContext("2d");
    document.addEventListener("keydown",keyPush);
    var fps=30;
    setInterval(update,1000/fps);
    setInterval(spawn,600);

    if(1==1){
        enemy=new Image();
        enemy.src="data:image/png;base64,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";
    }
    
    document.addEventListener("mousemove", mouseMoveHandler, false);
    document.addEventListener("mousedown", mouseClickHandler, false);
};

player_x=100;
player_y=400;

player_dim=30;
player_speed=15;

shots_list=[];
shot_dim=4;
shot_speed=7;

enemy_list=[];
enemy_dim=20;
enemy_speed=2.5;

score=0;
lives=5;

function update(){
    pen.fillStyle="black";
    pen.fillRect(0,0,canvas.width,canvas.height);
    pen.drawImage(enemy,player_x-player_dim/2,player_y-player_dim/2,player_dim,player_dim);

    for(s=0;s<shots_list.length; s++){
        shots_list[s].y-=shot_speed;
        pen.drawImage(enemy,shots_list[s].x-shot_dim/2,shots_list[s].y-shot_dim/2,shot_dim,shot_dim);
        
    
        for(e=enemy_list.length-1;e>=0; e--){
            var diff_x = Math.abs(enemy_list[e].x - shots_list[s].x);
            var diff_y = Math.abs(enemy_list[e].y - shots_list[s].y);
            var dist = Math.sqrt(diff_x * diff_x + diff_y * diff_y);
            if (dist < (shot_dim + enemy_dim) / 2) {
                enemy_list.splice(e, 1);
                score+=1;
            }
        }
    }

    for(e=0;e<enemy_list.length; e++){
        enemy_list[e].y+= enemy_speed;
        pen.drawImage(enemy,
        enemy_list[e].x - enemy_dim / 2,enemy_list[e].y - enemy_dim / 2,enemy_dim,
        enemy_dim);
        var diff_x=Math.abs(enemy_list[e].x-player_x);
        var diff_y=Math.abs(enemy_list[e].y-player_y);
        var dist=Math.sqrt(diff_x*diff_x+diff_y*diff_y);
        if(enemy_list[e].x < 0){
            shots_list=[];
            enemy_list=[];
            player_x=player_y=100;
            lives-=1;
            
        }
        if(dist<player_dim+enemy_dim/2){
            shots_list=[];
            enemy_list=[];
            player_x=player_x=100;
            lives-=1;
           
        }
    }
    
    if(lives==0){
        score=0;
        lives=5;
        pen.font=50+"px Verdana";
        pen.fillStyle="red";
        pen.fillText("Game Over",230,320);
    }       

    pen.font=20+"px Verdana";
    pen.fillStyle="yellow";
    pen.fillText("Score:",10,20);
    pen.fillText(score,80,20);
    pen.fillText("Lives:",screen.width-50,screen.height-50);
    pen.fillText(lives,80,450)
    
}

function keyPush(evt){
    switch(evt.keyCode){
        case 32:
            shots_list.push({ x: player_x, y: player_y });
            break;
    }

}
function mouseMoveHandler(e) {
        player_x=e.clientX;
}

function mouseClickHandler(e) {
    if(e.button===0){
        shots_list.push({y:player_y,y:player_x});
    }
}
function spawn(){
    enemy_list.push({x:Math.random()*canvas.width,y:0});
}
