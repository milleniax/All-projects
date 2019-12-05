$(".circle").animate({'width':'500px','height':'500px'},3000);
//$(".circle").text("Hello");
let circle = document.querySelector(".circle");
function checkDiv(){
    if(circle.style.width == '500px'){
    $('.circle').html("<p>hello world</p>").children().css({'position':'absolute','left':"50%",'top':"50%","transform":'translate(-50%,-50%)','margin':'0px',"color":"white",'font-size':'40px'});
}
else{
    setTimeout(checkDiv,50);
}
}
checkDiv();
