$(function(){
    //$('h1').css({'color': 'pink'});  //document.querySelector('h1');
    $('h1').hover(function(){
        $(this).toggleClass('violet');
        $('h1').on('click',function(){
            $(this).toggleClass('yellow');
        })
    })
    
    $('.left').css({'background' : 'green'})
    $('.left').mouseenter(function()
    {
        $(this).text('On').css({'text-align':'center'})
    })
    $(' div div:nth-child(2)').css({'background' : 'yellow'})

    let color = $('.left').data('color');
    console.log(color);

    $('button').on('click',function(){
        alert("Saved");
    });
    $('input[name = "name"]').keyup(function(){
        let value = $(this).val();

        $('input[type = "submit"]').val(value);
        if (value == "close"){
            $('form').hide(1000);
        }
        else if(value == "newHTML"){
            let newHTML = "<div class='triangle'></div>"
            $('form').html(newHTML);
            $('.circle').after(newHTML);
            $(".circle, .triangle").wrap('<div class="figures">');
        }
     
    });
    $('input[type = "radio"]').mouseenter(function(){
        let value = $(this).attr('value');

        alert(value);
    });
    $('.circle').mouseenter(function(){
        $(this).animate({'margin-left': '80%','opacity':'0.3'},1000);
    })
    $(window).resize(function(){
        let width = $(this).width();
        console.log(width);
    })
    console.log($('.content').html());
});
